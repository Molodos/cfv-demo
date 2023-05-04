__author__ = "Michael Weichenrieder"

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", title="Jinja and Flask")


if __name__ == "__main__":
    app.run(port=8080)
