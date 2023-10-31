# Hello World App
from flask import Flask
app=Flask(__name__)
@app.route("/") #That means: anytime someone visits my webpage, just return the 2 lines to them:
def hello():
    return "Hello World"

#Create a function that will return the second page and assign a URL 
# route to the second function with decorator @app.route("/") 
@app.route("/second")
def second():
    return "<h2>This is the second page</h2>"
@app.route("/third/subthird")
def third():
    return "<h3>This is the subpage of third page</h3>"

#create a dynamic url that takes id number dynamically and return with a 
# message which shows id of the page
@app.route("/fourth/<string:id>")
def fourth(id):
    
    if id.isdigit():
        return f"The id of the page is {id}"
    else:
        return f"not a valid id"
        
#Run the flask app
app.run(debug=False)
  