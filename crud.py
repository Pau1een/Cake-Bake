"""CRUD operations."""

from model import db, User, Favorite_recipe, connect_to_db


def create_user(fname, lname, email, password):
    """Create a new user and add it to database."""

    new_user= User(
        fname=fname, 
        lname=lname, 
        email=email,
        password=password,
        )

    return new_user


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def update_user_profile(fname, lname, email, password):
    """Save and update user profile."""

    updated_profile = User(fname=fname, lname=lname, email=email, password=password)

    return updated_profile


def save_as_favorite(user_id, favorite_name, favorite_img, favorite_ingredients, favorite_source, recipe_link):
    """Save and return a favorite."""

    favorite_recipe = Favorite_recipe(user_id=user_id, favorite_name=favorite_name, favorite_img=favorite_img, favorite_ingredients=favorite_ingredients, favorite_source=favorite_source,recipe_link=recipe_link)

    return favorite_recipe


def get_favorite_recipes_by_user(user_id):
    """Return favorite recipe by user id."""

    return Favorite_recipe.query.filter_by(user_id = user_id).all()


def save_review(review):
    """ Save a review. """

    review = Favorite_recipe.query.get(review)

    db.session.add(review)
    db.session.commit()

    return review



if __name__ == "__main__":
    from server import app

    connect_to_db(app)
