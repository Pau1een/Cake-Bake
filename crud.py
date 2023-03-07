"""CRUD operations."""

from model import db, User, Recipe, Review, connect_to_db


def create_user(fname, lname, email, password):
    """Create a new user and add it to database."""

    new_user= User(
        fname=fname, 
        lname=lname, 
        email=email,
        password=password,
        )

    db.session.add(new_user)
    db.session.commit()

    return new_user


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def create_recipe(recipe_name, recipe_text, date_baked, ingredients):
    """Create a recipe."""

    new_recipe= Recipe(
        recipe_name=recipe_name,
        recipe_text=recipe_text,
        date_baked=date_baked,
        ingredients=ingredients,
    )

    db.session.add(new_recipe)
    db.session.commit()

    return new_recipe


def get_recipe_by_name(recipe_name):
    """Return a recipe by name."""

    return Recipe.query.filter_by(recipe_name = recipe_name).first()


def get_review_by_recipe_id(recipe_id):
    """Return review by a recipe id."""

    return Review.query.filter_by(recipe_id = recipe_id).all()


def get_review_by_score(score):
    """Return review by score."""

    return Review.query.filter_by(score = score).all()


def create_review(recipe_id, review_user, score):
    """Create and return a new review."""

    review_user = Review(
        recipe_id=recipe_id,
        review_user=review_user,
        score=score
        
    )

    db.session.add(review_user)
    db.session.commit()

    return review_user


def update_review(recipe_id, new_review_user, new_score):
    """ Update a review given recipe name and the updated score. """

    review = Review.query.get(recipe_id)
    review.score = new_score
    review.review_user = new_review_user

    db.session.add(review)
    db.session.commit()

    return review


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
