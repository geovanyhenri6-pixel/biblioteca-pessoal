from flask import Flask
from config import Config
from database import init_db, close_db
from routes.auth import auth_bp
from routes.livros import livros_bp

app = Flask(__name__)
app.config.from_object(Config)
app.teardown_appcontext(close_db)
app.register_blueprint(auth_bp)
app.register_blueprint(livros_bp)

@app.cli.command("init-db")
def init_db_command():
    init_db()
    print("Banco inicializado.")