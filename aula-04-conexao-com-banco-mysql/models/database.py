# Importando o SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Criando uma instancia do SQLAlchemy
# Carregando o SQLAlchemy em uma váriavel
db = SQLAlchemy()

# Criando a classe para representr a entidade Games no Banco de Dados (tabela: games)
class Game(db.Model):
    # Colunas da tabela
    # FLoat é decimal pra preco
    # Chave primária
    id = db.Column(db.Integer, primary_key=True) 
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(150))
    plataforma = db.Column(db.String(150))
    preco = db.Column(db.Float) 
    quantidade = db.Column(db.Integer)
    
# Método construtor (atributos que serão usados pelos objetos)
def __init__(self, titulo, ano, categoria, plataforma, preco, quantidade):
    self.titulo = titulo
    self.ano = ano
    self.categoria = categoria
    self.plataforma = plataforma
    self.preco = preco
    self.quantidade = quantidade