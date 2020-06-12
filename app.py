from flask import Flask
from  flask_socketio import SocketIO,send


app=Flask(__name__)
app.config['SECERET_KEY']="mykey"
socketio =SocketIO(app,cors_allowed_origins="*")


@socketio.on ('triget_even')
def handleMessage(msg):
    print('Message',msg)
    send(msg,broadcast=True)



if __name__=='__main__':
    socketio.run(app)