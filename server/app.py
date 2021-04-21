from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "code-boy to the rescue!!!!"

@app.route("/g30tse")
def test():
    return "gotcha!"

if __name__ == "__main__":
    app.run()