"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud, model ,server

os.system("dropdb cake")
os.system("createdb cake")

model.connect_to_db(server.app)
model.db.create_all()

# Load recipe data from JSON file
with open("data/recipes.json") as f:
    recipe_data = json.loads(f.read())

# Create recipes, store them in list to create fake reviews with them.
recipes_in_db = []
for rcp in recipe_data:
    recipe_name, recipe, ingredients = (
        rcp["recipe_name"],
        rcp["recipe"],
        rcp["ingredients"],
    )

    date_baked = datetime.strptime(rcp["date_baked"], "%Y-%m-%d")

    db_recipe = crud.create_recipe(recipe_name, recipe, date_baked, ingredients)
    recipes_in_db.append(db_recipe)


# Create 10 users; each user will make 10 ratings
for n in range(10):
    email = f"user{n}@test.com"  
    password = "test"
    fname = n

    user = crud.create_user(fname, email, password)

    print(user)

    for _ in range(10):
        random_recipe = choice(recipes_in_db)
        score = randint(1, 5)

        rating = crud.create_rating(1, random_recipe.recipe_id, score)
