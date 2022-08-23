import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from .auth import auth
from .routes import routes

app.register_blueprint(routes, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')



from manutd import routes  # noqa