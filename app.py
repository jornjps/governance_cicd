from flask import Flask, render_template, request
from random import randrange
import os

app = Flask(__name__)

quote = [
    "I'm going to make him an offer he can't refuse.",
    "Toto, I've got a feeling we're not in Kansas anymore.",
    "Go ahead, make my day.",
    "May the Force be with you.",
    "You talking to me?",
    "I love the smell of napalm in the morning.",
    "You can't handle the truth!",
    "Round up the usual suspects.",
    "I'll be back",
    "You've got to ask yourself one question: 'Do I feel lucky?' Well, do ya, punk?",
    "Oh no!,   Anyway"
]
movie = [
    "The Godfather, 1972",
    "The Wizard of Oz, 1939",
    "Sudden Impact, 1983",
    "Star Wars, 1977",
    "Taxi Driver, 1976",
    "Apocalypse Now, 1979",
    "A Few Good Men, 1992",
    "Casablanca, 1942",
    "The Terminator, 1984",
    "Dirty Harry, 1971",
    "Jeremy Clarkson, Top Gear"


]


@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == "GET":
        return render.remplate('input.html')
    if request.method == 'POST':
        getal = (randrange(9))
        return render_template('template_file_name.html', quote=quote[getal], movie=movie[getal])


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
