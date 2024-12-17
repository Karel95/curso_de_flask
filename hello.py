from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_():
    return "<h1>Hello, World!</h1>"
