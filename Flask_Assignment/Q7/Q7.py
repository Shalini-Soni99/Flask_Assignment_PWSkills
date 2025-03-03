#7. Integrate a SQLite database with Flask to perform CRUD operations on a list of items
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DATABASE = 'items.db'

# Initialize database
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS items (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL)''')

@app.route('/')
def index():
    with sqlite3.connect(DATABASE) as conn:
        items = conn.execute('SELECT * FROM items').fetchall()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    name = request.form.get('name')
    if name:
        with sqlite3.connect(DATABASE) as conn:
            conn.execute('INSERT INTO items (name) VALUES (?)', (name,))
        return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('DELETE FROM items WHERE id = ?', (item_id,))
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
