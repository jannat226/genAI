from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI()

# response = client.responses.create(
#     model="gpt-4o",
#     input="Write a one-sentence bedtime story about a unicorn."#zero shot prompt
# )

#system prompt ---> control the behavior of the model
response = client.chat.completions.create(
    model ='gpt-4',
    messages=[
        {"role":"user","content":"2*2=?"}
    ]
)
print(response.choices[0].message.content)
