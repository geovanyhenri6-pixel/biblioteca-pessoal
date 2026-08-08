from database import get_db

#---------------------- CRIAR LIVROS -------------------------

def criar_livro(usuario_id, titulo, autor):
    db = get_db()
    cursor = db.execute(
        "INSERT INTO livros (usuario_id, titulo, autor) VALUES (?, ?, ?)",
        (usuario_id, titulo, autor)
    )

    db.commit()
    return cursor.lastrowid

#---------------------- LISTAR LIVROS -------------------------

def listar_livros_usuario(usuario_id, status=None):
    db = get_db()
    if status is None:
        cursor = db.execute(
            "SELECT * FROM livros WHERE usuario_id = ?",
            (usuario_id,)
        )
    else:
        cursor = db.execute(
            "SELECT * FROM livros WHERE usuario_id = ? AND status = ?",
            (usuario_id, status)
        )

    return cursor.fetchall()


#--------------------- ATUALIZAR STATUS -----------------------

def atualizar_status(livro_id, status, nota=None):
    db = get_db()

    cursor = db.execute(
        "UPDATE livros SET status = ?, nota = ? WHERE id = ?",
        (status, nota, livro_id)
    )

    db.commit()

#--------------------- REMOVER LIVRO -------------------

def remover_livro(livro_id):
    db = get_db()

    cursor = db.execute(
        "DELETE FROM livros WHERE id = ?",
        (livro_id,)
    )

    db.commit()

#--------------------- ESTATISTICA ----------------------- 

def estatistica_usuario(usuario_id):
    db = get_db()

    resultado_total = db.execute(
        "SELECT COUNT(*) AS total FROM livros WHERE usuario_id = ?",
        (usuario_id,)
    ).fetchone()

    resultado_lidos = db.execute(
        "SELECT COUNT(*) AS lidos FROM livros WHERE usuario_id = ? AND status = 'lido'",
        (usuario_id,)
    ).fetchone()

    resultado_media = db.execute(
        "SELECT AVG(nota) AS media FROM livros WHERE usuario_id = ? AND status = 'lido'",
        (usuario_id,)
    ).fetchone()

    return {
    "total": resultado_total["total"],
    "lidos": resultado_lidos["lidos"],
    "media": resultado_media["media"]
}

#--------------------- BUSCAR LIVRO ------------------------

def buscar_livro_por_id(livro_id):
    db = get_db()
    cursor = db.execute(
        "SELECT * FROM livros WHERE id = ?",
        (livro_id,)
    )
    livro = cursor.fetchone()
    return livro