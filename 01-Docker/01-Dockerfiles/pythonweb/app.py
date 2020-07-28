from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"



@app.route("/amit")
def hello_amit():
    return "Hello EveryOne, Welcome to Docker Demo"

@app.route("/info")
def hello_info():
    html = "<h2>Hello World</h2>"\
           "<b>HostName:</b> {hostname}<br/>"\
           "<b>FQDN:</b> {fqdn}"
    return html.format(hostname=socket.gethostname(),fqdn=socket.getfqdn())

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=8081)
