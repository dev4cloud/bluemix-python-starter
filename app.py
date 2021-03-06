from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Software Development for Cloud Computing!"

port = os.getenv('PORT', 5000)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(port))
