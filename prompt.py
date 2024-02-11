prompt_query = """
Use the information given below to answer the subsequent question. 
The information contains one or more Questions and top relevant text chunks for those questions
as well as their corresponding confidence score (in the range of 0 to 1; 1 meaning high confidence) 

For example:
Question 1:
How old is Aaron?
[['aaron is 50 years old', 0.6], ['Aaron goes to hiking', 0.2]]

Here is the actual information:
{information}

Using the above actual information answer the questions in the following format:

'''answer
Question: How old is Aaron?
Answer: Aaron is 50 years old

Question: Who is Aaron?
Answer: Aaron is a mathematician

'''

Do not consider the above example in the answer.
Do not change the format of the answer. 
Answers should be word to word match if the question is a word to word match.
If the answer cannot be found or If the answer is of low confidence, reply with question as a key and “Data Not Available” as a value. 
"""
