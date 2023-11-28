# import modules
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text


# setup flask app
app = Flask(__name__)

# Configure required environmental variables for SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./email.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the DB
db = SQLAlchemy(app)
app.app_context().push()

# - drop users table if exists, create new users table and add some rows for sample
drop_table = 'DROP TABLE IF EXISTS users;'
db.session.execute(text(drop_table))

users_table = """ 
CREATE TABLE users(
username VARCHAR NOT NULL PRIMARY KEY,
email VARCHAR);
"""
db.session.execute(text(users_table))

insert_data = """
INSERT INTO users
VALUES
	("Tuba", "tuba@amazon.com" ),
	("Ethan", "ethan@micrasoft.com"),
	("mostafa", "mostafa@facebook.com"),
    ("sait", "sait@tesla.com"),
    ("busra","busra@google");
"""
db.session.execute(text(insert_data))
db.session.commit()



# - Write a function named `emails` which finds email addresses by keyword using `GET` and `POST` methods,
# - using template files named `emails.html` given under `templates` folder
# - and assign to the static route of ('/')
@app.route("/", methods=["GET", "POST"])
def emails():
    if request.method == "GET":
        return render_template("emails.html", show_result=False)
    else:   # request.method == "POST"
        user_name = request.form["user_keyword"]
        user_emails = find_emails(user_name)
        return render_template("emails.html", show_result=True, keyword=user_name, name_emails=user_emails)
    

# - Write a function named `find_emails` which find emails using keyword from the user table in the db,
# - and returns result as tuples `(name, email)`.
def find_emails(username):
    query = f"""
    SELECT * FROM users WHERE username like '%{username}%';
    """
    result = db.session.execute(text(query))
    user_emails = [(row[0], row[1]) for row in result]
    if not any(user_emails):
        user_emails = [("Not Found", "Not Found")]
    return user_emails    


# - Write a function named `add_email` which inserts new email to the database using `GET` and `POST` methods,
# - using template files named `add-email.html` given under `templates` folder
# - and assign to the static route of ('/add')

@app.route

# - Write a function named `insert_email` which adds new email to users table the db.
# - Add a statement to run the Flask application which can be reached from any host on port 80.
if __name__ == "__main__":
    app.run(debug=True)