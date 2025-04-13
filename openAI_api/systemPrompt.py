from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()
systemPrompt = """
You are a helpful assistant that can answer questions and provide information.
You will be given a question, and you should respond with a clear and concise answer.

Example:
User: What is the capital of France?
Assistant: The capital of France is Paris.FunFact: The Eiffel Tower is located in Paris.
User: What is the capital of Germany?
Assistant: The capital of Germany is Berlin.FunFact: The Berlin Wall once divided the city into East and West.
"""
response = client.responses.create(
    model="gpt-4o",
    input=[
        {
            "role": "system",
            "content": systemPrompt
        },{
            "role": "user",
            "content": "What is 2*2"
        }
    ]
)

print(response.output_text)