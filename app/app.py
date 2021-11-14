from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import DevelopConfig, ProductConfig
from posts.blueprint import posts


app = Flask(__name__, static_folder="static")
app.config.from_object(DevelopConfig)
db = SQLAlchemy(app)

app.register_blueprint(posts, url_prefix='/post')
