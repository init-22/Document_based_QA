# Document based Question Answering

### Solution Flow:
1) Taking document and questions from user. 
2) Creating the embeddings for the document.
3) Creating embeddings for the questions. 
4) Taking a similarity score of each question and chunk of a document. 
5) Passing the top N chunks along with the questions to the LLM. 
6) LLM generating the response.


### How to improve it further? :</br> 
- Store chat history, use it for analytics, see what and where the LLM is giving wrong or hallucinated responses.
- Deciding the chunk size is important, some iterations have to be done on that.
- There could be different ways to match the embeddings for example. Divide embedding and also maintain their indexes to know the relative position. Once the matching score is higher, pass the more nearest neighbour chunks for better context. (eg. index-1, index, index+1)
- If the model can accommodate high token_len(GPT 128k, 32k) , pass the matching chunk + index or line number along with the entire document to allow the LLM to reason from entire knowledge.
- If the answer is not found in the document, ask the user if they prefer answers from the web, use serpapi, duckduckgo etc.
- Also, you can pass the summary of the document instead of a whole document. Let the LLM generate a summary of the entire document or summary of chunked documents (point 4)
- Sometimes users don't ask specific questions, in those scenarios, ask follow up questions, or let the LLM rephrase the question.
- Add agents who can read the answer, think and reiterate if the answer is not satisfactory.
- If you are already aware of the segment of the data, eg. healthcare; finetune on healthcare related data.
