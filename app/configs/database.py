from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    # Importe as suas models de uma maneira que faça sentido. Por exemplo: Em uma relação N:N, importe as
    # tabelas que são referenciadas na relação N:N e, após isso, importe a tabela pivô. Se você tentar importar
    # a tabela pivô primeiro, a mesma não terá suas dependências satisfeitas para formar a relação N:N, gerando
    # um erro
