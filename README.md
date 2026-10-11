# Scramble Word Game

A word-unscrambling game built for robot-supported learning at UNBC's Social Robotics Lab.
Children play on a touchscreen while a social robot guides them; the game was used at a
children's summer camp, and the activity informed our HRI '26 paper,
[*Social Robots on the Loose*](https://doi.org/10.1145/3757279.3785580).

## What it does
- Picks and scrambles words at random, scores each answer, and moves players through levels
- Saves game state and each child's interactions with the Django ORM, so results can be analysed later
- Runs on a local server with no internet connection

## Tech stack
Python · Django · HTML · CSS · JavaScript

## Run it locally
```bash
git clone https://github.com/piyushdaryanani/Scramble-Word-Game.git
cd Scramble-Word-Game
python3 -m venv venv && source venv/bin/activate
pip install django
python3 manage.py migrate
python3 manage.py runserver
```
Then open http://127.0.0.1:8000 in a browser.
