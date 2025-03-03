# Develop a Flask app that uses URL parameters to display dynamic content.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Home Page</h1><p>Try visiting /user/yourname</p>"

@app.route('/user/<name>')
def user(name):
    return f"<h1>Hello, {name.capitalize()}!</h1><p>Welcome to your profile page.</p>"

@app.route('/product/<int:product_id>')
def product(product_id):
    return f"<h1>Product Page</h1><p>Product ID: {product_id}</p>"

if __name__ == '__main__':
    app.run(debug=True)