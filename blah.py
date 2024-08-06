import requests
import google.generativeai as genai


# Replace YOUR_API_KEY with your actual API key
API_KEY = "AIzaSyBB7-NFo2xh4RlNH7CU4sX3a4CW2zdeHSE"

print('Enter a prompt:')
user_prompt:str = input()

# Set the request body
body = {
    "contents": [
        {
            "parts": [
                {
                    "text": user_prompt
                }
            ]
        }
    ]
}

# Set the request headers
headers = {
    "Content-Type": "application/json"
}

# Set the request URL
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={}".format(API_KEY)

#Send the request
response = requests.post(url, json=body, headers=headers)
json_response = response.json()
text_value = json_response['candidates'][0]['content']['parts'][0]['text']
print(f'{'AI Response: '}{text_value}')


