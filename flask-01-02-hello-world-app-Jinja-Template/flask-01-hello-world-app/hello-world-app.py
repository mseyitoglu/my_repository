# Hello World App
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "<h1> Hello World </h1>"
#Create a function second which returns a string This is the second page and 
# assign a URL route the second function with decorator @app.route('/second').
@app.route("/second")
def second():
    return "<h2> This is the second page</h2>"

@app.route("/fourth/<string:id>")
def fourth(id):
    if id.isdigit():
        return f"the id of this page is {id}"
    else:
        return "Not a valid id"


#run the flask app
app.run(debug=False)