
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Sample data
love_messages = [
    "You are my today and all of my tomorrows.",
    "Just thinking about you makes my heart smile.",
    "Every love story is special, but ours is my favorite.",
]

date_ideas = [
    "Stargazing with a blanket and wine.",
    "Cooking a fancy dinner together at home.",
    "A walk through a botanical garden followed by dessert.",
]

gift_ideas = {
    "new": ["A handwritten letter + their favorite candy", "A playlist of songs that remind you of them"],
    "serious": ["A personalized necklace", "A weekend getaway", "A custom photo album"],
    "longterm": ["A love journal", "A framed star map of your anniversary night", "A surprise experience day"]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_love_message')
def get_love_message():
    return jsonify(message=random.choice(love_messages))

@app.route('/get_date_idea')
def get_date_idea():
    return jsonify(idea=random.choice(date_ideas))

@app.route('/get_gift', methods=['POST'])
def get_gift():
    stage = request.json.get('stage', 'new')
    return jsonify(gift=random.choice(gift_ideas.get(stage, gift_ideas['new'])))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
