from openai import OpenAI
import os


def chat(prompt):
    client = OpenAI(api_key=os.getenv("DS_APIKEY"), base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
        stream=False
    )
    return response.choices[0].message.content