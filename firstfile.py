from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
user_input = input("HUMAN INPUT:")
#f = open("oneshotprompt.txt", "r")
f = open("fewshotprompt.txt", "r")
instructions = f.read()
f.close()


response = client.responses.create(
    model="gpt-4o",
    input=[
        {
            "role": "user",
            "content": "hi my name is aryan and i am a software engineer"
        },
        {
            "role": "assistant",
            "content": "Hi Aryan! It's great to meet you. How can I assist you today?"
        },
        {
            "role": "user",
            "content": user_input
        }]
)

print(response.output[0].content[0].text)