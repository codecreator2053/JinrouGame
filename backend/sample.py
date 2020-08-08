from pathlib import Path

from flask import Flask, render_template, request, redirect, url_for, session

static_folder = Path.cwd()

app = Flask(__name__, template_folder=str(static_folder.parents[0]), static_folder=str(static_folder.parents[0] / "resources"))

app.secret_key = 'A0Zr9foijaoe090'

@app.route("/")
def main():
    if "username" in session:
        print("Hello " + str(session['username']))
        return render_template('home.html')
    return redirect(url_for('login'))


@app.route('/login', methods=['POST'])
def login():
    session['username'] = request.form['username']
    return redirect(url_for('main'))


@app.route('/login', methods=['GET'])
def login_view():
    return """
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    """

if __name__ == "__main__":
    app.run()
