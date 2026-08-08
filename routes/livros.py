from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from routes.auth import login_required
from models.livro import (
    listar_livros_usuario,
    criar_livro,
    atualizar_status,
    remover_livro,
    buscar_livro_por_id,
)


livros_bp = Blueprint("livros", __name__)

#----------------------- LISTAR -----------------------------

@livros_bp.route("/livros")
@login_required
def listar():
     
    usuario_id = session["usuario_id"]
    livros = listar_livros_usuario(usuario_id)

    return render_template("livros/lista.html", livros=livros)

#----------------------- ADICIONAR LIVRO --------------------

@livros_bp.route("/livros/novo", methods=["GET", "POST"])
@login_required
def novo():

    if request.method == "POST":
        usuario_id = session["usuario_id"]
        titulo = request.form.get("titulo")
        autor = request.form.get("autor")

        criar_livro(usuario_id, titulo, autor)
        flash("Livro adicionado com sucesso!")

        return redirect(url_for('livros.listar'))
    return render_template('livros/form.html')

#---------------------- EDITAR ------------------------------

@livros_bp.route("/livros/editar/<int:livro_id>", methods=["GET", "POST"])
@login_required
def editar(livro_id):

    livro = buscar_livro_por_id(livro_id)

    if livro is None or livro["usuario_id"] != session["usuario_id"]:
        flash("Esse livro não existe.")

        return redirect(url_for('livros.listar'))

    if request.method == "POST":
        status = request.form.get('status')
        nota_raw = request.form.get("nota")
        nota = float(nota_raw) if nota_raw else None

        atualizar_status(livro_id, status, nota)
        flash("Status atualizados!")

        return redirect(url_for('livros.listar'))
    return render_template('livros/form.html', livro=livro)

#--------------------- REMOVER -----------------------------------

@livros_bp.route("/livros/remover/<int:livro_id>", methods=["POST"])
@login_required
def remover(livro_id):

    livro = buscar_livro_por_id(livro_id)

    if livro is None or livro["usuario_id"] != session["usuario_id"]:
        flash("Esse livro não existe.")

        return redirect(url_for('livros.listar'))

    remover_livro(livro_id)
    flash("Livro removido.")
    return redirect(url_for('livros.listar'))