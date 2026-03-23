# Cometário dem Python
# Importando o Flask na aplicação
from flask import Flask, render_template 
#Render template renderiz as paginas HTML

# Carregando o Flask em uma variável 
# Declarando variável no Python
app = Flask(__name__, template_folder='views')
# __name__ é uma variável de ambiente de phyton que tem o nome do módulo atual

# Criando a rota principal do site 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/games')
def games():
    # criando uma variável
    titulo = "Silk song"
    ano = 2025
    categoria = "Metroidvania"
    
    jogadores = ["Eduardo", "Vitor", "André", "Caio"]
    return render_template('games.html', titulo=titulo, ano=ano, categoria=categoria, jogadores=jogadores)



@app.route('/consoles')
def consoles():
    
    titulo = "Consoles"
    consoles = ["switch", "Playstation5", "Xbox", "Pc"]
    return render_template('consoles.html', titulo=titulo, consoles=consoles)
# def serve para criar funções no pythone home é o nome da função



# Iniciando o servidor web
if __name__ == '__main__':
    app.run(debug=True) #Ligando modo de depuração, reinicia automático
# .run inicia um servidor
# verificando se o app.py for o arquivo principal, ele inicia o servidor

# Ctrl + " = abre o terminal
# python app.py + enter = running...ip(local)
# Ctrl + clicar no ip -> not found ( navegador)
# porta padrão no python -> :5000
# Ctrl + C -> parar o servidor
