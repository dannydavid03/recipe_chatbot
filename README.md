#  Recipe Chatbot

A simple Flask web application that helps users find recipes based on ingredients and cuisine mentioned in their messages. It uses basic NLP techniques to extract relevant information and return matching recipes.

---

## 🧠 Features

- Accepts user input via chat interface
- Extracts ingredients and cuisine using NLP
- Matches user input against a dataset of recipes
- Returns top 5 matching recipes
- Simple web interface with Flask

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone git@github.com:dannydavid03/recipe_chatbot.git
cd recipe_chatbot
```
2. Set up a virtual environment (optional but recommended)
```bash
python3 -m venv venv
source venv/bin/activate
```
4. Install dependencies
```bash
pip install -r requirements.txt
```
6. Run the app
```bash
python app.py
```
Then open your browser and go to:
http://127.0.0.1:5000

💬 Example Usage

User Input:

Can you show me some Italian recipes with tomatoes and basil?
Bot Output:
Returns a list of up to 5 recipe titles that match the criteria.

⚙️ Technologies Used

Python 3
Flask
Custom NLP with simple keyword/entity extraction
JSON-based recipe data
📚 Data Source

Recipe data is sourced from:
🔗 https://github.com/dpapathanasiou/recipes

🛠️ TODO / Improvements

 Replace basic NLP with spaCy or NLTK for better entity extraction
 Add filtering by cooking time, difficulty, or dietary preference
 Improve frontend UI (CSS, chat flow)
 Add tests for extraction and recipe matching
 Dockerize the application for easier deployment
📄 License

This project is open source and available under the MIT License.


