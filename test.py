import openai

# APIキーの設定
openai.api_key = "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"

# プロンプト
prompt = input("入力: ")

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1024,
    temperature=0.5,
)
print(prompt+response['choices'][0]['text'])



#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