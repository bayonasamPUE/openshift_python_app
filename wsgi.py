import os
from flask import Flask
from flask import render_template
import socket
import random

application = Flask(__name__)

color_codes = { 
        "red":"#e74c3c",
        "green":"16a085",
        "blue":"#2980b9"
        }

color = random.choice(list(color_codes.keys()))

@application.route("/")
def main():
	return render_template("index.html", color=color, hostname=socket.gethostname(), background=color_codes[color])
	#return "Hello World!"
    
if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=80)
    application.run()


