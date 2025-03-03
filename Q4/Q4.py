#4. Create a Flask app with a form that accepts user input and displays it.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"<h1>Hello, {name}!</h1>"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
