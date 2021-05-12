from flask import Flask, redirect, url_for, render_template, request, Response
import algo as algo

app = Flask(__name__)

@app.route("/target", methods=["POST","GET"])
def login():
    response = Response()
    response.headers["Access-Control-Allow-Origin"] = "*"
    
    result = algo.scan(algo.convertToArray(request.form["content"]))
    responsedata = '"verdict": "' + str(result[0]) + '", "confidence": "' + str(round(algo.getScore(), 2)) + '"'

    response.set_data('{' + responsedata + '}')
    return response

if __name__ == "__main__":
    app.run(debug=True)
