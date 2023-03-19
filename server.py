from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db, db
import crud
import os
import requests
from pprint import pprint
from pprint import pformat
import json
from jinja2 import StrictUndefined
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route('/create_user')
def show_search_form():
    """Show form to create account"""

    return render_template('create_account.html')


@app.route('/create_account', methods=["POST"])
def make_user():
    """Create a new user account."""

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
        session["user_id"] = user.user_id
        flash(f"Hello {user.fname}!")

        return render_template('user_homepage.html')


@app.route("/logout")
def logout_user():
    """Log out user."""
    # Remove user from session when user clicks "logout" 
    session.clear()
    flash("You have logged out.")
    return redirect('/')


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

    app_key = os.environ['EDAMAM_KEY']
    app_id = os.environ['APP_ID']

    print(app_key)
    print(app_id)

    keyword = request.args.get('keyword', '')
    excluded = request.args.get('excluded-food')
    print(keyword)
    url = 'https://api.edamam.com/api/recipes/v2'
    payload = {'type': 'public',
            'q': f"{keyword},cake",
            'app_id':  app_id,
            'app_key': app_key,
            'field': ['label', 'source', 'image', 'url', 'ingredientLines'],

}
    # response = requests.get('https://api.edamam.com/api/recipes/v2?type=public&q=%22cake%22%2C%20keyword&app_id=9f63074f&app_key=9d021611986e18cf28f394015533320c&field=uri&field=label&field=image&field=source&field=url&field=ingredientLines')
    response = requests.get(url, params=payload)
    data = response.json()

    if excluded:
        payload['excluded'] = excluded

    response = requests.get(url, params=payload)
    data = response.json()

    if 'hits' in data:
        recipes = data['hits']
    else:
        recipes = []

    return render_template('search_result.html', pformat=pformat, data=data, results=response, recipes=recipes)


@app.route('/box')
def view_saved_recipes():
    """Show saved recipes"""
    user_id = session.get("user_id")
    display = crud.get_favorite_recipes_by_user(user_id)

    return render_template('recipe_box.html', recipes=display)


@app.route("/save_recipe", methods=["POST",])
def save_recipes():
    """Save a recipe to recipe box"""

    favorite_name = request.json["favorite_name"]
    favorite_img = request.json["favorite_img"]
    favorite_ingredients = request.json["favorite_ingredients"]
    favorite_source = request.json["favorite_source"]
    recipe_link = request.json["recipe_link"]
    user_id = session.get('user_id')

    existing_recipe = crud.get_favorite_recipes_by_link(recipe_link, user_id)
    
    if existing_recipe:
        return "Recipe already saved"

    else:
        favorite_recipe = crud.save_as_favorite(user_id, favorite_name, favorite_img, favorite_ingredients, favorite_source, recipe_link)
        db.session.add(favorite_recipe)
        db.session.commit()

    return "Added to your recipe box!"


# @app.route('/save_review', methods=['POST'])
# def save_review():
#     review = request.form.get("review")
#     review = crud.save_review(review)

#     db.session.add()
#     db.session.commit()
#     flash("Review/notes sucessfully saved")

#     return "Saved"


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
