# Document based Question Answering

### Solution Flow:
1) Taking document and questions from user. 
2) Creating the embeddings for the document.
3) Creating embeddings for the questions. 
4) Taking a similarity score of each question and chunk of a document. 
5) Passing the top N chunks along with the questions to the LLM. 
6) LLM generating the response.


### How to improve it further? :</br>
- Ideal chunk size and overlap should be calculated based on few more examples text-embedding-ada-002 performs better on chunks containing 256 or 512 tokens. Source: https://www.pinecone.io/learn/chunking-strategies/
For this use case I am using chunk size of 256</br>
1 token == 4 characters in avg. so 256 tokens = 256*4 = 1024

- Turning a document into embeddings in runtime should be avoided, if a user already has a data we can convert it into embeddings and then store it into a vector database, so the inference would be optimized.
Also, I could've stored the data in the .csv file for now and if the user is passing the same file over and over then I could've just used it from that stored file and passed it to the LLM to save time but not sure if its a good idea, what if the user don't want us to save the data?

- Prompt can also be improveed, security checks can be added in the prompt if required in order to prevent prompt leaking. 

- Why only OpenAI? 
A modular LLM framework can be created which can let us switch between different LLMs without much hassel. 
