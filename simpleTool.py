from openai import OpenAI
from dotenv import load_dotenv
import os
import requests
import json


load_dotenv()
client = OpenAI()

def get_weather(zip_code):
    api_key = os.getenv("OPEN_WEATHERMAP_API_KEY")
    country_code = "us"  # You can change this to the appropriate country code if needed
    url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={api_key}"
    result = requests.get(url)
    response = result.json()
    return response


tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather for a given zip code",
                "parameters": {
            "type": "object",
            "properties": {
                "zip_code": {
                    "type": "string",
                    "description": "The zip code to get the weather for"
                }
            },
            "required": ["zip_code"],
        },
        "required": ["zip_code"] 
    }
]

user_query = input("HUMAN INPUT: ")
response = client.responses.create(
    model="gpt-4o",
    input=user_query,
    tools=tools
)

for item in response.output:
    if item.type == "function_call":
        arguments = json.loads(item.arguments)
        if item.name == "get_weather":
            weather_info = get_weather(arguments["zip_code"])
            print("Weather Information: ", weather_info)