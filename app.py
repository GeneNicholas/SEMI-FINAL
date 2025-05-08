from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return ('<h1>GENE NICHOLAS MADRON!'
            ' 1st 25'
            ' System Integration'
            ' Semi-Final Exam </h1>')
