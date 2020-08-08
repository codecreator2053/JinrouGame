from pathlib import Path

from flask import Flask, render_template

static_folder = Path.cwd()

app = Flask(__name__, template_folder=str(static_folder.parents[0]), static_folder=str(static_folder.parents[0] / "resources"))

@app.route("/")
def main():
    return render_template("home.html")

if __name__ == "__main__":
    app.run()
