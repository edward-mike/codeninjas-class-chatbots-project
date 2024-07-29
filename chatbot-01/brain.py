# step 1: import openai
from openai import OpenAI

# step 2: translator establish connection to openai
translator = OpenAI(
    api_key="your_api_key",
)

# step 4: translate and get response
def chatbot_brain(user_question):
    response = translator.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{
            "role":"user",
            "content": user_question
        }]
    )

    return response.choices[0].message.content