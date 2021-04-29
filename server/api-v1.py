from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/target", methods=["POST","GET"])
def login():
    if request.method == "POST":

        #result = "pulls the result from the algorithm"
        #result could be formatted as a list
        #return "returns desired string format for the json
        

def find_results():
    #do something


if __name__ == "__main__":
    app.run(debug=True)
