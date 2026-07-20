from flask import Flask, render_template
from flashcards import flashcards
import random



app = Flask(__name__)



@app.route("/")
def home():
    kaart = random.choice(flashcards)
    
    return render_template("index.html", vraag=kaart["vraag"], antwoord=kaart["antwoord"])

if __name__ == "__main__":
    app.run(debug=True)