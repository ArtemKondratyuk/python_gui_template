import json
import random
import os
import sys

def load_phrases(filename="phrases.json"):
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    file_path = os.path.join(base_path, filename)
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def get_random_phrase(mood, data):
    mood = mood.strip().lower()
    if mood in data:
        return random.choice(data[mood])
    return "Такого настроения Я не знаю. Хорошего тебе дня!"