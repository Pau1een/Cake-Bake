from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
import crud
import os
# import requests
from pprint import pprint
from pprint import pformat
import json
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# apikey = os.environ['EDAMAM_KEY']
# apiid = os.environ['APP_ID']

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route('/create_user')
def show_search_form():
    """Show search form"""

    return render_template('create_account.html')


@app.route("/create_account", methods=["POST"])
def create_user():
    """Create a new user."""

    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    print(user)
    if user:
        flash("An account already exists with that email. Try again.")
        return redirect("/")
    else:
        user = crud.create_user(fname, lname, email, password)
        flash("Account created! Success!")

    return render_template("login.html")



# @app.route("/login", methods=["POST"])
# def process_login():
#     """Process user login."""

#     email = request.form.get("email")
#     password = request.form.get("password")

#     user = crud.get_user_by_email(email)
#     if not user or user.password != password:
#         flash("The email or password you entered was incorrect.")
#     else:
#         # Log in user by storing the user's email in session
#         session["user_email"] = user.email
#         flash(f"Welcome back, {user.fname}!")

#     return redirect("/")








# @app.route('/reviews')
# def search_reviews_by_recipe_name():
#     """Search for a review by recipe name"""

#     reviews = crud.get_review_by_recipe_name()

#     return render_template('reviews_recipe_name.html', reviews=reviews)


# @app.route('/find_recipes/search')
# def find_recipes():
#     """Search for recipes on EDAMAM"""

#     keyword = request.args.get('keyword', '')

#     url = 'https://api.edamam.com/api/recipes/v2'
#     payload = {'apikey', 'apiid'}


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
