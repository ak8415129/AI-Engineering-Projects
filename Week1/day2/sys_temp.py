import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq 

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)   
model="llama-3.3-70b-versatile"
role="user"
# prompt="I Love you"
# message_system = {
#     "role": "system", 
#     "content": "You are my Girlfriend"
# }
message_system = {
    "role": "system", 
    "content": "You are my brand manager"
}
message = {
    "role": role, 
    "content": "Suggest a  food brand for me"
}
messages = [message_system, message]
# response = client.chat.completions.create(model=model, messages=messages)
response = client.chat.completions.create(model=model, messages=messages,temperature=0.7)

# print(response)
print("---------------------------------------------------------------------")
print(response.choices[0].message.content)



