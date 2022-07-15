from app.blueprints.main.models import Car
from flask import redirect, render_template, url_for
from flask_login import current_user

from . import bp as app


@app.route('/')
def home():
    # check if user is logged in
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    cars = Car.query.all()
    cars.sort(key=lambda car: car.date_created, reverse=True)
    context = {"cars": cars}
    return render_template('index.html', **context)


@app.route('/about')
def about():
    return render_template('about.html')
