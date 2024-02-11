import json
import os
import re

from pypdf import PdfReader
from tqdm import tqdm

from embeddings import Embedding
from openai_api import OpenAI_api
from prompt import prompt_query


def get_multiple_questions(num_questions):
    questions = []
    for i in range(num_questions):
        question = input("Enter question {}: ".format(i + 1))
        questions.append(question)
    return questions


def preprocess_document(document, embedding_obj, chunk_size=256, chunk_overlap=70):
    embedding_list = []
    document_info = ""

    # Read the entire document using PdfReader and convert it to a string
    reader = PdfReader(document)
    number_of_pages = len(reader.pages)

    for i in range(number_of_pages):
        document_info += reader.pages[i].extract_text()

    # Chunk size is an experimental number depending on the type of content,
    # but model like text-embedding-ada-002 performs better on chunks containing 256 or 512 tokens.
    # Source: https://www.pinecone.io/learn/chunking-strategies/
    # 1 token == 4 characters in avg. so 256 tokens = 256*4 = 1024

    chunk_size *= 4
    i = 0
    while i < len(document_info) - chunk_size:
        current_info = document_info[i : i + chunk_size]
        # adding overlap
        i = i + (chunk_size - chunk_overlap)
        embedding_list.append(
            [current_info, embedding_obj.get_embeddings(current_info)]
        )

    return embedding_list


def main(openai_api, embedding_obj, document, questions_list, top_n_matches):
    print("\n\nCreating Embeddings from the document")
    embedding_list = preprocess_document(document, embedding_obj)
    print("\n\nMatching question embeddings with the document embeddings")
    matched_output = embedding_obj.get_matched_embeddings(
        questions_list, embedding_list, top_n=top_n_matches
    )
    prompt = prompt_query.format(information=matched_output)
    print("\n\nHold on, Providing the answer in a minute...")
    result = openai_api.ask(prompt)
    print("\n\nResponse:\n")

    questions = re.findall(r"Question:\s*(.*?)(?:\n|$)", result)
    answers = re.findall(r"Answer:\s*(.*?)(?:\n|$)", result)
    json_obj = {}
    for i in range(len(questions)):
        json_obj[questions[i]] = answers[i]
    print(json_obj)


if __name__ == "__main__":
    openai_key = ""
    openai_api = OpenAI_api(openai_key)
    embedding_obj = Embedding(openai_key)
    top_n_matches = 5  # Top n matches of the embeddings from the document

    print(
        "\nI can help you get answers to your questions based on the document provided by you!\n"
    )

    document = input("\nPlease provide the document: ")

    num_questions = int(
        input("\n\nHow many questions do you want to ask on this document? ")
    )
    questions_list = get_multiple_questions(num_questions)

    main(openai_api, embedding_obj, document, questions_list, top_n_matches)
