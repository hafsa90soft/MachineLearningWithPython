from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'magical-quest-key-2024'  # Updated secret key

@app.route('/', methods=['GET', 'POST'])
def number_guessing_game():
    # Initialize game state
    if 'secret_number' not in session:
        session['secret_number'] = random.randint(1, 100)
        session['attempts'] = 0
        session['high_score'] = session.get('high_score', float('inf'))
    
    message = None
    
    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            
            if guess < 1 or guess > 100:
                message = "🎯 Please guess a number between 1 and 100!"
            else:
                session['attempts'] += 1
                
                if guess == session['secret_number']:
                    # Update high score
                    if session['attempts'] < session['high_score']:
                        session['high_score'] = session['attempts']
                    
                    message = f"🎉 Congratulations! You found the magical number in {session['attempts']} attempts! "
                    message += f"(Best: {session['high_score']} attempts)"
                    
                    # Reset game but keep high score
                    session.pop('secret_number')
                    session.pop('attempts')
                elif guess < session['secret_number']:
                    message = "↗️ The magical number is higher! Try again..."
                else:
                    message = "↙️ The magical number is lower! Try again..."
                
        except ValueError:
            message = "⚠️ Please enter a valid number!"
            if 'attempts' in session:
                session['attempts'] -= 1
            
    return render_template('game.html', message=message)

@app.route('/reset')
def reset_game():
    session.clear()
    return redirect(url_for('number_guessing_game'))

if __name__ == "__main__":
    app.run(debug=True)
 