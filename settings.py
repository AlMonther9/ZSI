from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify




DATABASE = {
    'user': 'root',
    'pw': 'toor',
    'db': 'air_data',
    'host': 'mokhtar-Machine',
    'port': '3306',
}


# DB_URL = f"mysql+pymysql://{DATABASE['user']}:{DATABASE['pw']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['db']}"
DB_URL = f"sqlite:///db.sqlite3"
# SECRET_KEY = "soon to make forms and ui "


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL