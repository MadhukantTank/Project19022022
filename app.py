from flask import Flask
import socket
import datetime
app = Flask(_name_)
@app.route('/')
def hello_world():
    hostname = socket.gethostname()
    time = datetime.datetime.now().strftime("%m/%d/%Y,%H:%M:%S")
    return 'Welcome from '+hostname+' , at '+time
