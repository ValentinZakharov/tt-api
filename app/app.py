from flask import Flask
from .models import db
from .controllers import api

app = Flask(__name__)
app.config.from_pyfile('config.py')

api.init_app(app)
db.init_app(app)

if __name__ == '__main__':
    app.run()
