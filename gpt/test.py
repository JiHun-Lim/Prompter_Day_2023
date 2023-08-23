import pandas as pd
import numpy as np
import openai

# 발급받은 API 키 설정
OPENAI_API_KEY = "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"

# openai API 키 인증
openai.api_key = OPENAI_API_KEY

# 모델 - GPT 3.5 Turbo 선택
model = "gpt-3.5-turbo"

data_midterm = pd.read_csv("midterm.csv")
data_final = pd.read_csv("final.csv")
data_hw1 = pd.read_csv("homework1.csv")

midterm_chapter = data_midterm["chapter_name"]
final_chapter = data_final["chapter_name"]
hw1_problem = data_hw1["Problem"]

answers = []

for i in range(len(data_hw1)):

    # 질문 작성하기
    # query = "Give me a question of '" + midterm_chapter[i] + "' and give me a answer about it."
    query = "Give me a solution of '" + hw1_problem[i] + "'."

    # 메시지 설정하기
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": query},
    ]

    response = openai.ChatCompletion.create(model=model, messages=messages)
    answer = response["choices"][0]["message"]["content"]
    answers.append([hw1_problem[i], answer])

answers_df = pd.DataFrame(answers)
answers_df.to_csv("answers.csv", index=False)
