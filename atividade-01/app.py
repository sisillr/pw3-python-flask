# Comentário em Python.
# Importando o Flask na aplicação.
from flask import Flask, render_template
# render_template renderia as páginas HTML

# Carregando o Flask em uma variável.
# Declarando variável no Python.
app = Flask(__name__, template_folder='views')
# __name__ é uma variável de ambiente (que já existem) Python que tem o nome do módulo atual.

#CRIANDO A ROTA PRINCIPAL DO SITE
@app.route('/')
#def serve ára criar funções no python
def home():
    return render_template('index.html')

# GAMES

@app.route('/lista')
def lista():
    return render_template('lista.html')
    
# CONSOLES

@app.route('/formulario')
def formulario():   
    return render_template('formulario.html')
    

# Iniciando o servidor web (ligamos dentro ao inves de usar o xampp).
# .run (inicia um servidor).
if __name__ == '__main__':
    app.run(debug=True) # Ligando o Modo de Depuração (reinicia automático)
    # Verificando se app.py for o arqquivo principal ele inicia o servidor.