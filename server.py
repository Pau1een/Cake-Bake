from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
import crud
import os
import requests
from pprint import pprint
from pprint import pformat
import json
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

api_key = os.environ['EDAMAM_KEY']
app_id = os.environ['APP_ID']

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route('/create_user')
def show_search_form():
    """Show search form"""

    return render_template('create_account.html')


@app.route('/create_account', methods=["POST"])
def make_user():
    """Create a new user."""

    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    
    if user:
        flash("An account already exists with that email. Try again.")
        return render_template('login.html')
    else:
        new_user = crud.create_user(fname, lname, email, password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account created! Success!")

        return redirect('/login_user')


@app.route('/login_user')
def show_login_form():
    """Show login form"""

    return render_template('login.html')


@app.route('/login', methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")
        #Check if user email / password is correct or existing
    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
        return redirect('/login_user')
    else:
        # Log in user by storing the user's email in session
        session["email"] = user.email
        session["password"] = user.password
        flash(f"Hello {user.fname}!")

        return render_template('user_homepage.html')


@app.route('/user_homepage')
def show_user_homepage():
    """Show user_homepage form"""

    return render_template('user_homepage.html')


@app.route('/form')
def show_form():
    """Show recipe search form"""

    return render_template('search_form.html')


@app.route('/recipes/search')
def edamam_search():
    """Search for cake recipes on EDAMAM"""

    api_key = os.environ['EDAMAM_KEY']
    app_id = os.environ['APP_ID']

    keyword = request.args.get('search-keyword', '')
    url = 'https://api.edamam.com/api/recipes/v2'

    response = requests.get('https://api.edamam.com/api/recipes/v2?type=public&q=cake&app_id=api_key&app_key=app_id&dishType=Desserts&random=true&field=&field=label&field=image&field=images&field=source&field=url&field=ingredientLines&field=ingredients&field=dishType')

    data = response.json()
    if '_links' in data:
        recipes = data['_links']['recipes']
    else:
        recipes = []


    return render_template('search_result_.html', pformat=pformat, data=data, results=recipes)



@app.route('/reviews')
def search_reviews_by_recipe_name():
    """Search for a review by recipe name"""

    reviews = crud.get_review_by_recipe_name()

    return render_template('reviews_recipe_name.html', reviews=reviews)



@app.route("/recipes/<recipe_name>/reviews", methods=["POST"])
def create_review(recipe):
    """Create a new review by recipe name."""

    cake_review = request.form.get("review")

    if  not cake_review:
        flash("Wait!  Did you forget to write your review?")
    else:
        cake_recipe = crud.get_recipe_by_name(recipe)

        cake_review = crud.create_review(recipe)
        db.session.add(cake_review)
        db.session.commit()

        # flash(f"You reviewed this recipe {score} out of 5.")

    return redirect(f"/recipes/{recipe}")



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
