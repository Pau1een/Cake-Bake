from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    password = db.Column(db.String(25), nullable=False)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=True)
    phone = db.Column(db.Integer(25), nullable=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    address = db.Column(db.String, nullable=True)

    reviews = db.relationship("Review", back_populates="users")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"


class Ingredient(db.Model):
    """An ingredient"""

    __tablename__ = "ingredients"

    ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ingredient_name = db.Column(db.String)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"), nullable=False)
    
    recipes = db.relationship("Recipe", back_populates="ingredients")

    def __repr__(self):
        return f"<Ingredient ingredient_id={self.ingredient_id} ingredient_name={self.ingredient_name}>"


class Recipe(db.Model):
    """A recipe"""

    __tablename__ = "recipes"

    recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    recipe_name = db.Column(db.String)
    recipe = db.Column(db.Text)
    date_baked = db.Column(db.DateTime)
    ingredients = db.Column(db.Integer, db.ForeignKey("ingredients.ingredient_id"), nullable=False)

    ingredients = db.relationship("Ingredient", back_populates="recipes")
    reviews = db.relationship("Review", back_populates="recipes")

    def __repr__(self):
        return f"<Recipe recipe_id={self.recipe_id} ingredients={self.ingredient_id}>"


class Review(db.Model):
    """A review"""

    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"), nullable=False)
    review = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    score = db.Column(db.Integer, nullable=False)
    
    users = db.relationship("User", back_populates="reviews")
    recipes = db.relationship("Recipe", back_populates="reviews")

    def __repr__(self):
        return f"<Review review_id={self.review_id} user_id={self.user_id}>"


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