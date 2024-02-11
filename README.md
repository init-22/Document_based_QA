##*Document based Question Answering*

Solution Flow:
1) Taking Document and questions from user. 
2) Creating the embeddings for the document. 
3)Creating embeddings for the questions. 
4) Taking a similarity score of each question and chunk of a document. 
5) passing the top N chunks along with the questions to the LLM. 
6) LLM generating the response.


Solution Flow:</br>
Ideal chunk size and overlap should be calculated based on few more examples text-embedding-ada-002 performs better on chunks containing 256 or 512 tokens. Source: https://www.pinecone.io/learn/chunking-strategies/
For this use case I am using chunk size of 256
1 token == 4 characters in avg. so 256 tokens = 256*4 = 1024

Turning a document into embeddings in runtime should be avoided, if a user already has a data we can convert it into embeddings and then store it into a vector database, so the inference would be optimized.
Also, I could've stored the data in the .csv file for now and if the user is passing the same file over and over then I could've just from that stored file and passed it to LLM to save time but its not always a good idea, what if the user dont want us to save the data. 

Prompt can also be improveed, security checks can be added in the prompt if required in order to prevent promp leaking. 

Why only OpenAI? 
A modular LLM framework can be created which can let us switch between different LLMs without much hassel. 