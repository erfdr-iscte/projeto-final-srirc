from flask import Flask
import socket
import time
import os

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    return f"API instance: {hostname}\n"

@app.route("/health")
def health():
    return "OK", 200

@app.route("/slow")
def slow():
    time.sleep(5)
    return "Delayed response\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
