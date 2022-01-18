# from flask import Flask
# from flask import request
# from flask import get
from flask import request
from .data_loader import data_loader
from . import app
#Flask Routes

#Set Up Data stuff
loader = data_loader()

recipes = loader.load()
#GET

@app.get("/recipes")
def get_recipe_names(recipes = recipes):
    response = list(recipes.keys())
    return {"recipeNames": response}

@app.get("/recipes/details/<name>")
def get_recipe(name,recipes = recipes):
    if name in recipes:
        recipe = recipes[name]
        return {"details":recipe}
    else:
        return "", 200

#POST

@app.post("/recipes")
def post_recipes(recipes = recipes,loader=loader):
    data = request.get_json(force=True)
    # We make a backup here, incase something happens
    # while we are writing the data to the JSON,
    # in which case we will roll back to the origional state of the dict
    # to avoid the two being out of sync
    backup_recipes = recipes.copy()
    if data.get("name") in recipes:
        return {"error":"Recipe already exists"},400
    else:
        try:
            recipes[data.get("name")]={"ingredients":data.get("ingredients"),
                                       "instructions":data.get("instructions")}
            loader.write(recipes)
        except Exception:
            # we dont really care what the exception is 
            # we're just gonna roll it back, and return a 500
            recipes = backup_recipes
            return {"error": "Error writing, rolling back"}, 500
        return "", 204

#PUT

@app.put("/recipes")
def update_recipe(recipes = recipes,loader=loader):
    data = request.get_json(force=True)
    # We make a backup here, incase something happens
    # while we are writing the data to the JSON,
    # in which case we will roll back to the origional state of the dict
    # to avoid the two being out of sync
    backup_recipes = recipes.copy()
    if data.get("name") not in recipes:
        return {"error": "Recipe doesn't exist"}, 404
    else:
        try:
            recipes[data.get("name")]["ingredients"] = data.get("ingredients")
            recipes[data.get("name")]["instructions"] = data.get("instructions")
            loader.write(recipes)
        except Exception:
            # we dont really care what the exception is 
            # we're just gonna roll it back, and return a 500
            recipes = backup_recipes
            return {"error": "Error writing, rolling back"}, 500
            
        return "", 204





