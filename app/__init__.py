from config import Config
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # connect Config class to our app instance
    app.config.from_object(Config)

    migrate = Migrate()

    # initialize instance of db
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints with our app instance
    from app.blueprints.api import bp as api_bp
    app.register_blueprint(api_bp)

    from app.blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.blueprints.blog import bp as blog_bp
    app.register_blueprint(blog_bp)

    from app.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
