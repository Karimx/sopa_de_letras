import os
from pathlib import Path

from flask import Flask, flash, redirect, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = os.path.join(os.path.curdir, "static")

filename = None


@app.route("/", methods=["GET", "POST"])
def load():
    global filename
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return "<H2>Loaded/<H2> go to /letter "
    return """
        <!doctype html>
        <title>Upload new Letter Soup</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=Upload>
        </form>
        """


filename_letter = None


@app.route("/letter", methods=["GET", "POST"])
def load_letter():
    global filename_letter
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)

        filename_letter = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename_letter))
        return "<H2>Loaded/<H2> go to /solve"
    return """
        <!doctype html>
        <title>Upload new Letter Soup</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=Upload>
        </form>
        """


@app.route("/solve")
def solve():
    global filename
    from sopa_solver import SopaSolver, loader

    f = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    print(f"Reading {f}")
    soup = loader.from_file(Path(f))
    letters = os.path.join(app.config["UPLOAD_FOLDER"], filename_letter)
    print(f"Reading letter file {letters}")
    letters_to_find = loader.read_to_find(Path(letters))
    solver = SopaSolver()
    solver.set_sopa(soup)
    result = [
        (letter, result)
        for letter, result in zip(letters_to_find, solver.find_words(letters_to_find))
    ]
    return f"<H3>{result}/<H3>"


if __name__ == "__main__":
    app.run()
