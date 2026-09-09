# Importando o SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# Criando uma instância do SQLAlchemy
# Carregando o SQLAlchemy em uma variável
db = SQLAlchemy()

# Criando a classe para representar a entidade Games no banco de dados (tabela: games)
class Game(db.Model):
    # Colunas da tabela
    # Chave primária
    id = db.Column(db.Integer, primary_key=True) 
    titulo = db.Column(db.String(150))
   
    # Método construtor (atributos que serão utilizados pelos objetos)
    def __init__(self, titulo):
        self.titulo = titulo
        
# Criando a classe para representar a entidade Games no banco de dados (tabela: games)
class Console(db.Model):
    # Colunas da tabela
    # Chave primária
    id = db.Column(db.Integer, primary_key=True) 
    nome = db.Column(db.String(150))
    fabricante = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)
    
    # Método construtor (atributos que serão utilizados pelos objetos)
    def __init__(self, nome, fabricante, ano, preco, quantidade):
        self.nome = nome
        self.fabricante = fabricante
        self.ano = ano
        self.preco = preco
        self.quantidade = quantidade
        
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    senha = db.Column(db.String(250), nullable=False)
    
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha