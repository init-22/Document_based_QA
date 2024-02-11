import openai
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  



class OpenAI_api:
    def __init__(self, key=None, temperature=0, model="gpt-3.5-turbo", **kwargs):
        self.temperature = temperature
        self.openai = openai
        self.model = model
        self.openai.api_key = key


    @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
    def ask(self, prompt):

        messages = [
                {"role": "system", "content": f"You are a helpful assistant who give precise anwers based on the provided data"},
                {"role": "user", "content": prompt},
            ]

        completion = self.openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
        )

        return completion.choices[0].message.content
