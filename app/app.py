from flask import Flask

from config import DevelopConfig, ProductConfig
from posts.blueprint import posts

app = Flask(__name__, static_folder="static")
app.config.from_object(DevelopConfig)
app.register_blueprint(posts, url_prefix='/post')
