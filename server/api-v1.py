from flask import Flask, redirect, url_for, render_template, request, Response, jsonify
import algo as algo

app = Flask(__name__)

@app.route("/target", methods=["POST","GET"])
def login():
    response = Response()
    response.headers["Access-Control-Allow-Origin"] = "*"
    

    #result = "pulls the result from the algorithm"
    #result could be formatted as a list
    #return "returns desired string format for the json"
    result = algo.scan(algo.convertToArray(request.form["content"]))

    responsedata = '"verdict": "' + str(result[0]) + '", "confidence": "' + str(round(algo.getScore(), 2)) + '"'
    response.set_data('{' + responsedata + '}')
    return response

def find_results():
    #do something
    pass

if __name__ == "__main__":
    app.run(debug=True)
