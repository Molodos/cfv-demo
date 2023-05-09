__author__ = "Michael Weichenrieder"

import json
import uuid
from os import path
from typing import Any

from flask import Flask, render_template, request, redirect

from cfv_demo.web_app.file_processor import FileProcessor

UPLOAD_PATH: str = path.join(path.dirname(path.realpath(__file__)), "uploads")
RESULT_PATH: str = path.join(path.dirname(path.realpath(__file__)), "results")

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route("/", methods=["GET"])
def home():
    """
    Main page
    """
    return redirect("/upload")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    """
    Upload page
    """
    if request.method == "POST":
        file_id: str = str(uuid.uuid4())
        file = request.files["file"]
        if file.filename != "":
            file.save(path.join(UPLOAD_PATH, f"{file_id}.bin"))
            FileProcessor.process(file_id=file_id, file_name=file.filename)
            return redirect(f"/entropy?file_id={file_id}")
        else:
            return redirect(f"/upload")
    else:
        return render_template("upload.html", site="Upload")


@app.route("/entropy", methods=["GET"])
def entropy():
    """
    Entropy results display page (or waiting)
    """
    file_id: str = request.args.get("file_id")
    if not path.isfile(path.join(RESULT_PATH, f"{file_id}.json")):
        return render_template("process.html", site="Entropy", file_id=file_id)
    else:
        file = path.join(RESULT_PATH, f"{file_id}.json")
        data: dict[str, Any] = json.load(open(file))
        return render_template("entropy.html", site="Entropy", data=data)


if __name__ == "__main__":
    """
    Init point of the web app
    """
    app.run(port=8080)
