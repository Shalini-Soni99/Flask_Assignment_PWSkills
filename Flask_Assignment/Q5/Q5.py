#5. Implement user sessions in a Flask app to store and display user-specific data.
from flask import Flask, session, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required to use sessions

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form.get('username')
        session['username'] = username  # Store username in session
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f"<h1>Welcome, {session['username']}!</h1><a href='/logout'>Logout</a>"
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove user data from session
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)