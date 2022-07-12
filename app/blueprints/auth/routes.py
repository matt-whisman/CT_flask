from flask import render_template
from . import bp as app


@app.route('login')
def login():
    user_dict = {
        "username": "username",
        "password": "password"
    }
    context = user_dict
    return render_template('login.html', **context)
