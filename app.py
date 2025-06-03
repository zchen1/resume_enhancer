from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

# 读取 API 密钥
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        resume = request.form["resume"]
        job = request.form["job"]

        prompt = f"请根据以下求职目标优化这份简历内容：\n\n目标岗位：{job}\n简历内容：{resume}"

        # 新版本的 API 调用方式（>=1.0）
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        result = chat_completion.choices[0].message.content

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
