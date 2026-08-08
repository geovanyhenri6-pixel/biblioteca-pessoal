from flask import render_template, request, redirect, url_for, session, Blueprint, flash
from models.usuario import buscar_usuario_por_email, criar_usuario, verificar_senha
from functools import wraps

auth_bp = Blueprint("auth", __name__)

#------------------ CADASTRO -----------------------

@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':

        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        if buscar_usuario_por_email(email):
            flash("Esse e-mail já está cadastrado.")
        else:
            criar_usuario(nome, email, senha)
            flash("Conta criada com sucesso!")
            return redirect(url_for('auth.login'))
    return render_template('cadastro.html')

#------------------ LOGIN -----------------------

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        user = buscar_usuario_por_email(email)

        if user is not None and verificar_senha(senha, user["senha_hash"]):
            session["usuario_id"] = user["id"]
            flash("Bem-Vindo(a)!")
            return redirect(url_for('livros.listar'))
        else:
            flash("Email ou senha inválidos.")
    return render_template('login.html')

#------------------ LOGOUT -----------------------

@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Sessão encerrada.")
    return redirect(url_for('auth.login'))

#----------------- LOGIN-REQUIRED ----------------
    
def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "usuario_id" not in session:
            flash("Faça o login para continuar.")
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return wrapper