from flask import Flask
from config import Config
from database import init_db, close_db

app = Flask(__name__)
app.config.from_object(Config)
app.teardown_appcontext(close_db)

@app.cli.command("init-db")
def init_db_command():
    init_db()
    print("Banco inicializado.")