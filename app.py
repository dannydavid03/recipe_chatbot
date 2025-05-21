from flask import Flask, request, jsonify, render_template
from nlp_utils import extract_entities
from load_recipes import load_all_recipes

app = Flask(__name__)

ALL_RECIPES = load_all_recipes()

def match_recipe(user_entities):
    results = []

    for recipe in ALL_RECIPES:
        ingredients = recipe.get("ingredients", [])
        title = recipe.get("title", "Unnamed Recipe").lower()

        if user_entities["ingredients"]:
            if not all(ing in ingredients for ing in user_entities["ingredients"]):
                continue
    
        if user_entities["cuisine"]:
            if user_entities["cuisine"] not in title:
                continue

        results.append(recipe)

    return results[:5] if results else [{"title": "No matching recipes found."}]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    entities = extract_entities(user_input)
    matched = match_recipe(entities)
    recipe_titles = [r["title"] for r in matched]
    return jsonify({"recipes": recipe_titles})


if __name__ == "__main__":
    app.run(debug=True)

