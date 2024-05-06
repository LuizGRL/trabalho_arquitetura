from flask import render_template
from app.models.produto import Produto

def cadastrar_produto(nome, preco):
    produto = Produto(nome, preco)
    return str(produto)

def renderizar_formulario_produto():
    return render_template("produto_form.html")
