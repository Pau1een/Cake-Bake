"""CRUD operations."""

from model import db, User, Recipe, Review, connect_to_db


def create_user(fname, lname, email, password):
    """Create a new user and add it to database."""

    new_user = User(fname=fname, lname=lname, email=email, password=password)

    db.session.add(new_user)
    db.session.commit()

    return new_user

# def get_user_by_email_password(email, password):
#     """Return a user by email and password."""
    
#     db.session.add(email, password)
#     db.session.commit()

#     return User.query.get(User)

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def create_recipe(recipe_name, recipe, date_baked, ingredients):
    """Create a recipe."""

    new_recipe= Recipe(
        recipe_name=recipe_name,
        recipe=recipe,
        date_baked=date_baked,
        ingredients=ingredients,
    )

    db.session.add(new_recipe)
    db.session.commit()

    return new_recipe


def get_recipe_by_name(recipe_name):
    """Return a recipe by name."""

    db.session.add(Recipe)
    db.session.commit()

    return Recipe.query.filter_by(recipe_name = recipe_name).first()


def get_review_by_recipe_name(recipe_name):
    """Return review by a recipe name."""

    db.session.add(Review)
    db.session.commit()

    return Review.query.filter_by(recipe_name = recipe_name).all()


def get_review_by_score(score):
    """Return review by score."""

    db.session.add(Review)
    db.session.commit()

    return Review.query.filter_by(score = score).all()


def create_review(recipe_name, user_id, date_baked, score):
    """Create and return a new review."""

    review = Review(
        recipe_name=recipe_name,
        user_id=user_id,
        date_baked=date_baked,
        score=score
        
    )

    db.session.add(review)
    db.session.commit()

    return review


def update_review(review_id, new_score):
    """ Update a review given review_id and the updated score. """

    review = Review.query.get(review_id)
    review.score = new_score

    db.session.add(review)
    db.session.commit()

    return review


def create_rating(user_id, recipe_id, score):
    """Create a score."""

    rating = Review(
    user_id = user_id,
    recipe_id=recipe_id,
    score=score
        
    )

    db.session.add(rating)
    db.session.commit()

    return rating


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
