from flask import Flask, request, send_file
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def index():
    return "Madam Dudu Natal Chart API is alive!"

@app.route("/chart")
def chart():
    return "Coming soon: chart drawing logic"

if __name__ == "__main__":
    app.run()
