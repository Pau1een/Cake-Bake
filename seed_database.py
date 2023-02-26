"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb cake")
os.system("createdb cake")

model.connect_to_db(server.app)
model.db.create_all()

# Load recipe data from JSON file
with open("data/recipes.json") as f:
    recipe_data = json.loads(f.read())

# Create recipes, store them in list so we can use them
# to create fake reviews
recipes_in_db = []
for recipe in recipe_data:
    recipe_name, recipe, ingredients = (
        recipe["recipe_name"],
        recipe["recipe"],
        recipe["ingredients"],
    )
    date_baked = datetime.strptime(recipe["date_baked"], "%Y-%m-%d")

    db_recipe = crud.create_recipe(recipe_name, recipe, ingredients)
    recipes_in_db.append(db_recipe)

model.db.session.add_all(recipes_in_db)
model.db.session.commit()

# Create 10 users; each user will make 10 ratings
for n in range(10):
    email = f"user{n}@test.com"  
    password = "test"

    user = crud.create_user(email, password)
    model.db.session.add(user)

    for _ in range(10):
        random_recipe = choice(recipes_in_db)
        score = randint(1, 10)

        rating = crud.create_rating(user, random_recipe, score)
        model.db.session.add(rating)

model.db.session.commit()