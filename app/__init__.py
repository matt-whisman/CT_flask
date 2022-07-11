from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        user_dict = {
            "username": "username"
        }
        context = user_dict
        return render_template('index.html', **context)

    @app.route("/about")
    def about():
        return render_template('about.html')

    @app.route("/login")
    def login():
        user_dict = {
            "username": "username",
            "password": "password"
        }
        context = user_dict
        return render_template('login.html', **context)

    @app.route("/register")
    def register():
        return render_template('register.html')

    @app.route("/blog")
    def blog():
        return render_template('blog.html')

    return app
