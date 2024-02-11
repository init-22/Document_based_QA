import openai
from scipy import spatial


class Embedding:
    def __init__(self, key=None, embedding_model="text-embedding-ada-002"):
        self.openai = openai
        self.openai.api_key = key
        self.embedding_model = embedding_model

    def get_embeddings(self, text, embedding_model="text-embedding-ada-002"):
        response = openai.embeddings.create(input=text, model=self.embedding_model)
        embedding = response.data[0].embedding
        return embedding

    def question_ranked_by_relatedness(
        self, question: str, embedding_info: list, top_n
    ):
        question_embedding = self.get_embeddings(question)

        result = []
        for i in range(len(embedding_info)):
            score = 1 - spatial.distance.cosine(
                question_embedding, embedding_info[i][1]
            )
            result.append([embedding_info[i][0], score])

        result.sort(key=lambda x: x[1], reverse=True)
        return result[:top_n]

    def get_matched_embeddings(self, questions, embedding_list, top_n=5):
        matched_output = ""
        for i in range(len(questions)):
            relatednesses = self.question_ranked_by_relatedness(
                questions[i], embedding_list, top_n=top_n
            )
            matched_output += (
                f"Question {i+1}:\n{questions[i]}:\n{str(relatednesses)}\n\n"
            )

        return matched_output
