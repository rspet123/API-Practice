import json

class data_loader:
    recipe_path = "app/resources/recipes.json"
    
    
    def __init__(self,path: str):
        recipe_path = path
    #our overloaded constructor, to make sure we can do other stuff, not just recipes
    def __init__(self):
        recipe_path = "app/resources/recipes.json"
        
    
    @classmethod
    def load(self):
        recipe_dict = {}
        with open(self.recipe_path,"r") as data_file:
            recipe_list = json.load(data_file).get("recipes")
        #It gives us a list, which is okay
        #but we kind of want it to be faster, and we want to be able to find
        #recipies quickly, without having to iterate through the list
        #So I'll turn it into a dict
        for recipe in recipe_list:
            recipe_dict[recipe["name"]] = {"ingredients":recipe["ingredients"],
                                           "instructions":recipe["instructions"]}
        return recipe_dict
    
    @classmethod 
    def load_specific(self,search: str):
        with open(self.recipe_path,"r") as data_file:
            return json.load(data_file).get(search)
    

        
    @classmethod
    def update_recipe(self, recipe: dict, updated_recipe: dict):
        for key, val in updated_recipe.items():
            recipe[key] = val
    
    @staticmethod
    def recipe_dict_to_list(recipe_dict: dict):
        recipe_list =[]
        for recipe_name in recipe_dict.keys():
           recipe_list.append({"name":recipe_name,
             "ingredients":recipe_dict[recipe_name]["ingredients"],
             "instructions":recipe_dict[recipe_name]["instructions"]
             })
        return recipe_list
        
    @classmethod
    def write(self, recipe_dict: dict):
        recipe_list = self.recipe_dict_to_list(recipe_dict)
        with open(self.recipe_path, "w") as data_file:
            json.dump({"recipes": recipe_list}, data_file, indent=2)



