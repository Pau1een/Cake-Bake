"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud, model, server

os.system("dropdb cake")
os.system("createdb cake")

model.connect_to_db(server.app)
model.db.create_all()



# Create 10 users
for n in range(10):
    fname = n
    lname = n
    email = f"user{n}@test.com"  
    password = "test"
    

    new_user = crud.create_user(fname, lname, email, password)

    print(new_user)



# Load recipe data from JSON file
# with open("data/recipes.json") as f:
#     recipe_data = json.loads(f.read())

# Create recipes, store them in list.
# recipes_in_db = []
# for rcp in recipe_data:
#     recipe_name, recipe_text, ingredients = (
#         rcp["recipe_name"],
#         rcp["recipe_text"],
#         rcp["ingredients"],
#     )

#     date_baked = datetime.strptime(rcp["date_baked"], "%Y-%m-%d")

#     db_recipe = crud.create_recipe(recipe_name, recipe_text, date_baked, ingredients)
#     recipes_in_db.append(db_recipe)





