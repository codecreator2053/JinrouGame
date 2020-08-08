import string
import random
from pathlib import Path

from flask import Flask, render_template, request, redirect, url_for, session

code_candidate = list(string.ascii_letters) + list(string.digits)

static_folder = Path.cwd()

app = Flask(__name__, template_folder=str(static_folder.parents[0]), static_folder=str(static_folder.parents[0] / "css"))

app.secret_key = 'A0Zr9foijaoe090'

@app.route("/", methods=['POST', 'GET'])
def top_page():
    session['room'] = ''.join(random.choices(code_candidate, k=4))
    return render_template('home.html')


@app.route("/<room_id>")
def main(room_id):
    if "username" in session:
        print("Hello " + str(session['username']))
        return render_template('home.html')
    return redirect(url_for('login', room_id=room_id))


@app.route('/<room_id>/login', methods=['POST'])
def login(room_id):
    session['username'] = request.form['username']
    return redirect(url_for('main', room_id=room_id))


@app.route('/<room_id>/vote', methods=['POST'])
def vote(room_id):
    """Recieve voting result

    Args:
        result: {'from': 'username1', 'to': 'username2'}
    """

    print(request.json['from'], request.json['to'])
    return redirect(url_for('main', room_id=room_id))


@app.route('/<room_id>/night_action', methods=['POST'])
def night_action(room_id):
    """Recieve night action

    Args:
        result: {'from': 'username1', 'to': 'username2'}
    """
    return redirect(url_for('main', room_id=room_id))


@app.route('/<room_id>/login', methods=['GET'])
def login_view(room_id):
    return """
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    """

if __name__ == "__main__":
    app.run()
