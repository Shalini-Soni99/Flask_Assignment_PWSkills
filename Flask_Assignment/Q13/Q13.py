#Implement notifications in a Flask app using websockets to notify users of updates.

from flask import Flask, render_template
from flask_socketio import SocketIO
import time
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('notifications.html')

def send_notifications():
    notifications = [
        "New message from Admin!",
        "System update scheduled at midnight.",
        "New user joined the chat!",
        "Reminder: Meeting at 3 PM today."
    ]
    while True:
        time.sleep(5)  # Send a notification every 5 seconds
        notification = notifications.pop(0)
        socketio.emit('notification', {'message': notification})
        notifications.append(notification)  # Rotate notifications

@socketio.on('connect')
def handle_connect():
    socketio.emit('notification', {'message': "Welcome! Stay tuned for updates."})

if __name__ == '__main__':
    threading.Thread(target=send_notifications, daemon=True).start()
    socketio.run(app, debug=True)
