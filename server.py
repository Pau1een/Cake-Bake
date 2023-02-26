from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!
@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route("/reviews")
def all_reviews():
    """View all reviews."""

    reviews = crud.get_review_by_user_id()

    return render_template("all_reveiws.html", reveiws=reviews)

    
if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
