from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import DevelopConfig, ProductConfig
from blog.blueprint import blog


app = Flask(__name__, static_folder="static")
app.config.from_object(DevelopConfig)
db = SQLAlchemy(app)

app.register_blueprint(blog, url_prefix='/blog')
