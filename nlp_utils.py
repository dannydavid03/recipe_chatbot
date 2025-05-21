import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(user_input):
    doc = nlp(user_input.lower())
    ingredients = []
    cuisine = None
    diet = None

    diet_keywords = ["vegan", "vegetarian", "gluten-free", "low-carb"]
    cuisines = ["italian", "mexican", "indian", "american", "asian"]

    for token in doc:
        if token.text in diet_keywords:
            diet = token.text
        if token.text in cuisines:
            cuisine = token.text
        if token.pos_ == "NOUN":
            ingredients.append(token.text)

    return {
        "ingredients": ingredients,
        "cuisine": cuisine,
        "diet": diet
    }

