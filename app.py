from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    return f'Случайное число: {random.randint(1, 10000)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
