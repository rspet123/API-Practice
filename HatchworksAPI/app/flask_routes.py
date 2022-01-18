# from flask import Flask
# from flask import request
# from flask import get
import logging
from flask import Flask
from flask import request
from .data_loader import data_loader
import time
app = Flask('')
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
    if data.get("name") in recipes:
        return {"error":"Recipe already exists"},400
    else:
        recipes[data.get("name")]={"ingredients":data.get("ingredients"),
                                   "instructions":data.get("instructions")}
        loader.write(recipes)
        return "", 204

#PUT

@app.put("/recipes")
def update_recipe(recipes = recipes,loader=loader):
    data = request.get_json(force=True)
    if data.get("name") not in recipes:
        return {"error": "Recipe doesn't exist"}, 404
    else:
        recipes[data.get("name")]["ingredients"] = data.get("ingredients")
        recipes[data.get("name")]["instructions"] = data.get("instructions")
        loader.write(recipes)
        return "", 204
        
#app.run(port=5000, debug=True)
#POST

#@app.post("/recipes")




