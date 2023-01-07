import openai
import key

openai.api_key = key.A

def chat(cmdInput):

    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = cmdInput,
        max_tokens = 2048,
        temperature = 0.9,
    )

    return response['choices'][0]['text']
    # return response
