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

## 📁 Project Structure

recipe_chatbot/
├── app.py # Main Flask application
├── nlp_utils.py # NLP utility to extract entities
├── load_recipes.py # Loads and processes recipes data
├── recipes/ # Directory containing raw recipe data
├── recipes.json # Processed recipe data (optional)
├── recipies.json # Possibly a typo/duplicate of recipes.json
├── templates/
│ └── index.html # HTML frontend
├── pycache/ # Python cache files
├── README.md # Project documentation
└── venv/ # Python virtual environment (optional)


---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone git@github.com:dannydavid03/recipe_chatbot.git
cd recipe_chatbot
2. Set up a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
If requirements.txt doesn't exist, install Flask manually:
pip install Flask
4. Run the app
python app.py
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


