from flask import render_template
from . import bp as app


@app.route('/')
def home():
    user_dict = {
        "username": "username"
    }
    context = user_dict
    return render_template('/app/templates/index.html', **context)


@app.route('/about')
def about():
    return render_template('/app/templates/about.html')
