from app import db
from app.blueprints.main.models import Car
from flask import request, redirect

from . import bp as app


@app.route('/submit-car', methods=['POST'])
def submit_car():
    make = request.form['make']
    model = request.form['model']
    year = request.form['year']
    color = request.form['color']
    price = request.form['price']

    user_id = 1
    new_car = Car(make=make, model=model, year=year,
                  color=color, price=price, user_id=user_id)
    db.session.add(new_car)
    db.session.commit()

    return redirect("localhost:5000")
