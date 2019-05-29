from flask import Flask
#import os
#from flask import render_template
#import socket

app = Flask(__name__)

@app.route("/")

#def main():
#    return render_template("index.html", hostname=socket.gethostname())

def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)

