from flask import Flask

from config import Config
from posts.blueprint import posts

app = Flask(__name__, static_folder="static")
app.config.from_object(Config)
app.register_blueprint(posts, url_prefix='/post')
