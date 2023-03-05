from flask import Flask, render_template, request
import openai
import os

openai.api_key = '#############' # 输入自己的api_key!!!!!!!!!!!!!!!!!!!!!!!
assert(openai.api_key)
app = Flask(__name__)

messages = []
@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])

def get_bot_response():
    message = request.form['message']
    messages.append({'role': 'user', 'content': message})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    response = completion.choices[0].message['content']
    print(response)
    return response

if __name__ == '__main__':
    app.run(debug=True)
