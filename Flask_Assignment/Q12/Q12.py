 #Build a Flask app that updates data in real-time using WebSocket connections.
from flask import Flask, render_template
from flask_socketio import SocketIO
import random
import time
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

data = {"value": 0}

@app.route('/')
def index():
    return render_template('index.html')

def generate_data():
    while True:
        time.sleep(2)
        data["value"] = random.randint(1, 100)
        socketio.emit('update', data)

@socketio.on('connect')
def handle_connect():
    socketio.emit('update', data)

if __name__ == '__main__':
    threading.Thread(target=generate_data, daemon=True).start()
    socketio.run(app, debug=True)
