# routes/blueprint.py
from flask import Blueprint, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit, send, join_room, leave_room
from datetime import datetime

bp_index = Blueprint("index", __name__, template_folder="templates")
socketio = SocketIO()

def on_connect():
    print('client connected')
    room = request.args.get('room')
    join_room(room)
    username = request.args.get('username')  
    message = f'{username} has joined the room.'
    emit('message', {'message': message, 'username': 'Server', 'room': room}, room=room)




@socketio.on('message')
def handle_message(data):
    print('Handling message...')
    message = data.get('message')
    username = data.get('username')
    timestamp = datetime.now().strftime("%H:%M:%S")
    formatted_message = f'{timestamp} - {username}: {message}'
    print('Received message:', formatted_message)
    room = data.get('room')
    emit('message', {'message': formatted_message, 'username': username, 'room': room}, room=room)



@socketio.on("join")
def on_join(data):
    username = data.get("username")
    room = data.get("room")
    join_room(room)
    message = f"{username} has entered the room."
    emit("message", {'message': message, 'username': 'Server', 'room': room}, room=room)

@socketio.on("leave")
def on_leave(data):
    username = data["username"]
    room = data["room"]
    leave_room(room)
    send("{} has left the room.".format(username), to=room)

@bp_index.route("/")
def index():
    return render_template("index.html")

@bp_index.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        username = request.form.get("username")
        room = request.form.get("room")
        return redirect(url_for("index.chat_room", username=username, room=room))
    else:
        return render_template("index.html")

@bp_index.route("/chat/<username>/<room>")
def chat_room(username, room):
    return render_template("chat.html", username=username, room=room)
