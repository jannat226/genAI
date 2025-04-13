from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

response = client.responses.create(
    model="gpt-4o",
    input=[
        {
            "role": "developer",
            "content": "Talk like a pirate."
        },
        {
            "role": "user",
            "content": "Are semicolons optional in JavaScript?"
        }
    ]
)

print(response.output_text)