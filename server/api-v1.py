from flask import Flask, redirect, url_for, render_template, request, Response

app = Flask(__name__)

@app.route("/target", methods=["POST","GET"])
def login():
    response = Response()
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.set_data('{"verdict": "true", "confidence": "0.92"}') #example

    #result = "pulls the result from the algorithm"
    #result could be formatted as a list
    #return "returns desired string format for the json"

    return response

def find_results():
    #do something
    pass

if __name__ == "__main__":
    app.run(debug=True)
