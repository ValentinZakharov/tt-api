import os

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') \
                          or 'postgresql://postgres:passw0rd@1@localhost:5438/postgres'
SQLALCHEMY_TRACK_MODIFICATIONS = False
ERROR_404_HELP = False
