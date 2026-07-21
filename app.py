from flask import Flask, render_template
#from flashcards import flashcards
import random
import json

with open("flashcards.json", "r", encoding="utf-8") as file:
    flashcards = json.load(file)



app = Flask(__name__)



@app.route("/")
def home():
    kaart = random.choice(flashcards)
    
    return render_template("index.html", vraag=kaart["question"], antwoord=kaart["answer"], options=kaart.get("options", []))

if __name__ == "__main__":
    app.run(debug=True)