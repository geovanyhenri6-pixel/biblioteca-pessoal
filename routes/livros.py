from flask import Blueprint, render_template, request, session
from routes.auth import login_required
from models.livro import listar_livros_usuario


livros_bp = Blueprint("livros", __name__)


@livros_bp.route("/livros")
@login_required
def listar():
     
    usuario_id = session["usuario_id"]
    livros = listar_livros_usuario(usuario_id)
    return render_template("livros/lista.html", livros=livros)