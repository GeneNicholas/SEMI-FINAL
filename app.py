import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return ('<h1>GENE NICHOLAS MADRON!'
            ' 1st 25'
            ' System Integration'
            ' Semi-Final Exam </h1>')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)