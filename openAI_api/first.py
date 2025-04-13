import json
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI()

# response = client.responses.create(
#     model="gpt-4o",
#     input="Write a one-sentence bedtime story about a unicorn."#zero shot prompt
# )

#system prompt ---> control the behavior of the model
systemPrompt = """
You are a helpful assistant that can answer questions and provide information.
You will be given a question, and you should respond with a clear and concise answer.
""" 

message=[
        {"role":"user","content":systemPrompt}
    ]
query = input(">")
message.append({'role':'assistant','content':query})

while True:
    response = client.chat.completions.create(
        model ='gpt-4',
        messages=message
    )
    parsed_response = json.loads(response.choices[0].message.content)
    message.append({'role':'assistant','content': json.dumps(parsed_response)})
    if parsed_response.get('step')!= "output":
        print(f"{parsed_response['step']}: {parsed_response['content']}")
        continue
    print(f"Final Output: {parsed_response['content']}")
    break
  
print(response.choices[0].message.content)
