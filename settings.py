from flask_sqlalchemy import SQLAlchemy
from flask import Flask


SEREVER_ADDRESS = '0.0.0.0'
PORT = 3000

DATABASE = {
    'user': 'root',
    'pw': 'admin',
    'db': 'air_data',
    'host': '127.0.0.1',
    'port': '3306',
}


DB_URL = f"mysql+pymysql://{DATABASE['user']}:{DATABASE['pw']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['db']}"
# DB_URL = f"sqlite:///db.sqlite3"
# SECRET_KEY = "soon to make forms and ui "


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
