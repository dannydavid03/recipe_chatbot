import os
import json

def load_all_recipes(recipe_dir='recipes/index'):
    recipes = []

    for root, _, files in os.walk(recipe_dir):
        for file in files:
            if file.endswith(".json"):
                try:
                    with open(os.path.join(root, file), 'r') as f:
                        data = json.load(f)
                        # Normalize data
                        data['ingredients'] = [ing.lower() for ing in data.get('ingredients', [])]
                        recipes.append(data)
                except Exception as e:
                    print(f"Error loading {file}: {e}")
    
    return recipes
