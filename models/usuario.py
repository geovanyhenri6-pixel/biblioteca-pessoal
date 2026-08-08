from werkzeug.security import generate_password_hash, check_password_hash
from database import get_db

def criar_usuario(nome, email, senha):
    senha_hash = generate_password_hash(senha)
    db = get_db()

    cursor = db.execute(
        "INSERT INTO usuarios (nome, email, senha_hash) VALUES (?, ?, ?)",
        (nome, email, senha_hash)
    )
    db.commit()

    return cursor.lastrowid

def buscar_usuario_por_email(email):
    db = get_db()
    cursor = db.execute(
        "SELECT * FROM usuarios WHERE email = ?",
        (email,)
    )
    user = cursor.fetchone()
    return user

def verificar_senha(senha_fornecida, senha_hash):
    return check_password_hash(senha_hash, senha_fornecida)