from flask import Flask
from  flask_socketio import SocketIO,send


app=Flask(__name__)
app.config['SECERET_KEY']="mykey"
socketio =SocketIO(app,cors_allowed_origins="*")


@socketio.on ('message')
def handleMessage(msg):
    'Any message event occur then this return to all its broadcast client'
    print('Message',msg)
    print("\n")
    send(msg,broadcast=True)



if __name__=='__main__':
    socketio.run(app)