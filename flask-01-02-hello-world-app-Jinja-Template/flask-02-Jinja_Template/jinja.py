# Using Jinja templates
# Import Flask and render_template modules.
# Create an object named app from imported Flask module.
# Create an index.html file under templates folder.
# Create a function named head which sends number number1 and number2 variables to the index.html. Use these variables into the index.html file.
# Assign a URL route the head function with decorator @app.route('/').
# Create an body.html file under templates folder.
# Create a function named number which sends number num1 and num2 and sum of them to the index.html. Use these variables into the body.html file. 
# Assign a URL route the number function with decorator @app.route('/sum').
# run the application in debug mode
# Connect the Hello World application from the web browser with localhost:5000 or 127.0.0.1:5000
# Save the complete code as jinja.py file under flask-02-Jinja_Template folder.
# Add and commit all changes on local repo
# Push all files to your remote repo on GitHub.

from flask import Flask, render_template

app =Flask(__name__)
# @app.route("/")
# def head():
#     return render_template("index.html", number1=10, number2=20)
# app.run(debug=False)

# @app.route("/number/<string:num1>/<string:num2>")
# def custom(num1, num2):
#     if num1.isdigit and num2.isdigit:
#         return render_template("index.html", number1=num1, number2=num2)
#     else:
#         return "this is not a valid input"
# app.run(debug=False)

@app.route("/sum/<string:num1>/<string:num2>")
def number(num1, num2):
        if num1.isdigit and num2.isdigit:
            sum=int(num1)+int(num2)
            return render_template("body.html", num1=num1, num2=num2, sum=sum)
        else:
            return "this is not a valid input"

app.run(debug=False)