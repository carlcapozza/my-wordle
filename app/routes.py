from flask import Flask, render_template, request, redirect, session, url_for
import random
from app.words import WORD_LIST

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = "supersecretkey"

@app.route('/')
def index():
    """Home page where users can start the game."""
    if 'target_word' not in session:
        return render_template('index.html', game_active=False)
    return render_template('index.html', game_active=True, attempts=session.get('attempts', []))

@app.route('/start', methods=['GET', 'POST'])
def start_game():
    session.clear()
    session['target_word'] = random.choice(WORD_LIST).upper()
    session['attempts'] = []
    return redirect('/')

@app.route('/guess', methods=['POST'])
def make_guess():
    """Handle a player's guess and show the result."""
    if 'target_word' not in session:
        return redirect(url_for('index'))

    guess = request.form.get('guess', '').upper()
    if len(guess) != 5 or not guess.isalpha():
        error_message = "Invalid input. Guess must be a 5-letter word."
        return render_template('index.html', game_active=True, attempts=session.get('attempts', []), error=error_message)

    target_word = session['target_word']
    feedback = []

    for i, letter in enumerate(guess):
        if letter == target_word[i]:
            feedback.append("green")
        elif letter in target_word:
            feedback.append("yellow")
        else:
            feedback.append("gray")

    # Update session attempts
    attempts = session.get('attempts', [])
    attempts.append({"guess": guess, "feedback": feedback})
    session['attempts'] = attempts

    if guess == target_word:
        attempts_count = len(session['attempts'])
        session.pop('target_word')
        session.pop('attempts')
        return render_template('result.html', result="win", attempts=attempts_count)

    if len(session['attempts']) >= 6:
        correct_word = session.pop('target_word')
        session.pop('attempts')
        return render_template('result.html', result="lose", correct_word=correct_word)

    return redirect(url_for('index'))

@app.route('/')
def game_status():
    guesses = session.get('attempts', [])
    return render_template('index.html', guesses=guesses)