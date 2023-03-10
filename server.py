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

    app_key = os.environ['EDAMAM_KEY']
    app_id = os.environ['APP_ID']

    print(app_key)
    print(app_id)

    keyword = request.args.get('keyword', '')
    print(keyword)
    url = 'https://api.edamam.com/api/recipes/v2'
    payload = {'type': 'public',
            'q': f"{keyword},cake",
            'app_id':  app_id,
            'app_key': app_key,
            'field': ['label', 'source', 'image', 'url', 'ingredientLines']

}
    # response = requests.get('https://api.edamam.com/api/recipes/v2?type=public&q=%22cake%22%2C%20keyword&app_id=9f63074f&app_key=9d021611986e18cf28f394015533320c&field=uri&field=label&field=image&field=source&field=url&field=ingredientLines')
    response = requests.get(url, params=payload)
    data = response.json()
    # print(data)
    if 'hits' in data:
        recipes = data['hits']
    else:
        recipes = []

    return render_template('search_result.html', pformat=pformat, data=data, results=response, recipes=recipes)



@app.route('/box')
def view_saved_recipes():
    """Show saved recipes"""

    return render_template('recipe_box.html')


@app.route('/reviews')
def search_reviews_by_recipe_name():
    """Search for a review by recipe name"""

    reviews = crud.get_review_by_recipe_name()

    return render_template('reviews_recipe_name.html', reviews=reviews)



@app.route("/recipe_reviews", methods=["POST"])
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


@app.route("/logout")
def logout_user():
    """Log out user."""

    # Remove user from session when user clicks "logout" 
    del session["user_id"]
    flash("You have logged out.")
    return redirect("/")




if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
