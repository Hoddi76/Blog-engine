from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import DevelopConfig, ProductConfig

app = Flask(__name__, static_folder="static")
app.config.from_object(DevelopConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import models

