from app import db
from app.blueprints.main.models import User
from flask import flash, redirect, render_template, request, url_for
from flask_login import login_user, logout_user

from . import bp as app


@app.route('/login', methods=['get', 'post'])
def login():
    if request.method == 'post':
        # return user filtered by email or None
        user = User.query.filter_by(email=request.form['email']).first()

        if user is None:
            flash(
                f"No user with email {request.form['email']}. Please register.", 'danger')

        # check if password is correct
        elif not user.check_mypassword(request.form['password']):
            flash('Incorrect password', 'danger')
        else:
            login_user(user)
            flash('User logged in successfully', 'success')
            return redirect(url_for('main.home'))
        return render_template('index.html')
    # indicates get request
    else:
        return render_template('login.html')


@app.route('/register', methods=['get', 'post'])
def register():
    if request.method == 'post':
        # get the user by email
        check_user = User.query.filter_by(email=request.form['email']).first()

        # if user is not None, they already exists
        if check_user is not None:
            flash('That user already exists', 'danger')
        else:
            # if passwords match, create a new user
            if request.form['password'] == request.form['confirm_password']:
                new_user = User(
                    email=request.form['email'],
                    password='',
                    username=request.form['username'],
                    first_name=request.form['first_name'],
                    last_name=request.form['last_name']
                )
                new_user.hash_my_password(request.form['password'])
                db.session.add(new_user)
                db.session.commit()
                flash('User created successfully, please login', 'success')
                return redirect(url_for('auth.login'))
            else:
                flash("Passwords don't match", "danger")
        return render_template('register.html')
    # for get request
    else:
        return render_template('register.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
