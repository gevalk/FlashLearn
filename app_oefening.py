from flask import flask, render_template
import random
import json


with open("flashcards.json", "r", encoding="utf-8") as file: