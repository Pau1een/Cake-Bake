from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(25), nullable=False)
    address = db.Column(db.String, nullable=True)

    reviews = db.relationship("Review", back_populates="users")
    favorites_recipes = db.relationship("Favorite_recipe", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} fname={self.fname} email={self.email}>"


class Recipe(db.Model):
    """A recipe"""

    __tablename__ = "recipes"

    recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#   user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=True)
    recipe_name = db.Column(db.String)
    recipe_text = db.Column(db.Text)
    ingredients = db.Column(db.Text)
    date_baked = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)

    reviews = db.relationship("Review", back_populates="recipe")

    def __repr__(self):
        return f"<Recipe recipe_id={self.recipe_id} recipe_name={self.recipe_name} recipe_text={self.recipe_text} date_baked={self.date_baked} reviews={self.reviews} ingredients={self.ingredients}>"

class Favorite_recipe(db.Model):

    __tablename__ = "favorite_recipes"

    favorite_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=True)
    favorite_name = db.Column(db.String)
    favorite_img = db.Column(db.String)
    favorite_ingredients = db.Column(db.String)
    favorite_source = db.Column(db.String)
    recipe_link = db.Column(db.String)

    user = db.relationship("User", back_populates="favorites_recipes")

    def __repr__(self):
        return f"<Favorite recipe id={self.favorite_id} by user_id={self.user_id} >"


class Review(db.Model):
    """A review"""

    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"), nullable=True)
    review_user = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    score = db.Column(db.Integer, nullable=True)
    
    users = db.relationship("User", back_populates="reviews")
    recipe = db.relationship("Recipe", back_populates="reviews")

    def __repr__(self):
        return f"<Review review_id={self.review_id} review_user={self.review_user} created_at={self.created_at} score={self.score}>"


def connect_to_db(flask_app, db_uri="postgresql:///cake", echo=False):
    """Connect to database."""

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = False
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app


    connect_to_db(app)