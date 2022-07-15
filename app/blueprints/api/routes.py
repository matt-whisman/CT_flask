from app import db
from app.blueprints.main.models import Car
from flask import flash, redirect, request, url_for
from flask_login import current_user

from . import bp as app


@app.route('/submit-car', methods=['post'])
def submit_car():
    make = request.form['make']
    model = request.form['model']
    year = request.form['year']
    color = request.form['color']
    price = request.form['price']

    # get the current logged in user
    user = current_user.id

    # create a new Car instance
    new_car = Car(make=make, model=model, year=year,
                  color=color, price=price, user_id=user.id)
    db.session.add(new_car)
    db.session.commit()

    # give success message
    flash('New car added successfully')

    return redirect(url_for('main.home'))
