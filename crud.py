"""CRUD operations."""

from model import db, User, Ingredient, Recipe, Review, connect_to_db


def create_user(fname, email, password):
    """Create and return a new user."""

    user = User(fname=fname, email=email, password=password)

    return user


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def get_ingredients_by_name(ingredient_name):
    """Return ingredients by name."""

    return Ingredient.query.all(ingredient_name)


def get_ingredients_by_recipe_id(recipe_id):
    """Return ingredients by a recipe id."""

    return Ingredient.query.get(recipe_id)


def create_recipe(recipe_name, recipe, ingredients):
    """Create and return a new recipe."""

    recipe = Recipe(recipe_name=recipe_name, recipe=recipe, ingredients=ingredients)

    return recipe


def get_recipe_by_name(recipe_name):
    """Return a recipe by name."""

    return Recipe.query.get(recipe_name)


def get_recipe_by_date_baked(date_baked):
    """Return a recipe by date baked."""

    return Recipe.query.get(date_baked)


def get_recipe_by_id(recipe_id):
    """Return a recipe by primary key."""

    return Recipe.query.get(recipe_id)


def get_recipe_by_ingredient(ingredients):
    """Return a recipe by ingredient."""

    return Recipe.query.get(ingredients)


def get_review_by_recipe_id(recipe_id):
    """Return review by a recipe id."""

    return Review.query.get(recipe_id)


def get_review_by_user_id(user_id):
    """Return review by a user id."""

    return Review.query.get(user_id)


def get_review_by_created_at(created_at):
    """Return review by a recipe id."""

    return Review.query.get(created_at)


def create_review(recipe, user_id, date_baked, score):
    """Create and return a new review."""

    review = Review(
        recipe=recipe,
        user_id=user_id,
        date_baked=date_baked,
        score=score
        
    )

    return review


def update_review(review_id, new_score):
    """ Update a review given review_id and the updated score. """
    review = Review.query.get(review_id)
    review.score = new_score

    return review


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
