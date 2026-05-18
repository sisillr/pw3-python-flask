# Cometário dem Python
# Importando o Flask na aplicação
from flask import Flask, render_template 
#Render template renderiz as paginas HTML
from controllers import routes
# Importando o PyMySQL
import pymysql
# Importando o Model de Games
from models.database import db, Game

# Carregando o Flask em uma variável 
# Declarando variável no Python
app = Flask(__name__, template_folder='views')
# __name__ é uma variável de ambiente de phyton que tem o nome do módulo atual

# definindo o nome do banco de dados
DB_NAME = 'thegames'

# Passando o nome do banco para o Flask
app.config['DATABASE_NAME'] = DB_NAME

# Passando o endereço do banco para o Flask-SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'

# enviando a variavel App (flask) para as rotas
routes.init_app(app)

# Iniciando o servidor web
if __name__ == '__main__':
    # Passando os dados e criando a conexão com o banco
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    
    # Tentando conexão com o banco
    try: 
        with connection.cursor() as cursor:
            #Cria o banco se ele não existir
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print("O banco de dados foi criado com sucesso!")
            
    except Exception as error:
        print(f"Erro ao criar o banco de dados: {error}")
    
    #Fechando conexão
    finally:
        connection.close()
        
    # Inicializar o SQLAlchemy
    db.init_app(app=app)
    with app.test_request_context():
        # Criando as atbelas
        db.create_all()
        #Iniciando o servidor
        app.run(debug=True)
    
    app.run(debug=True) #Ligando modo de depuração, reinicia automático
# .run inicia um servidor
# verificando se o app.py for o arquivo principal, ele inicia o servidor

# Ctrl + " = abre o terminal
# python app.py + enter = running...ip(local)
# Ctrl + clicar no ip -> not found ( navegador)
# porta padrão no python -> :5000
# Ctrl + C -> parar o servidor
