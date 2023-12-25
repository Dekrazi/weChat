from flask import Flask
from routes.blueprint import bp_index, socketio

app = Flask(__name__)
app.register_blueprint(bp_index)

app.config['SECRET_KEY'] = 'secret!'

if __name__ == "__main__":
    socketio.init_app(app)
    socketio.run(app, debug=True)
