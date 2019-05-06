import os
from flask import Flask
from flask import render_template
import socket
import random

application = Flask(__name__)


@application.route("/")
def main():
	return render_template("index.html", hostname=socket.gethostname())
	#return "Hello World!"
    
if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=80)
    application.run()


