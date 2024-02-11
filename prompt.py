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
Do not consider the above example in the answer, answer based on actual passed information.
Answers should be word to word match if the question is a word to word match.
If the answer cannot be found or If the answer is of low confidence, reply with “Data Not Available” along with that question. 


"""