from flask import Flask, render_template

# Carregando o Flask. 
# Como sua pasta de HTML se chama 'views', o parâmetro template_folder é essencial.
app = Flask(__name__, template_folder='views')

# ROTA PRINCIPAL (Home)
@app.route('/')
def home():
    return render_template('index.html')

# ROTA INDEX
@app.route('/index')
def index_page(): # Mudei o nome da função para não conflitar
    return render_template('index.html')

# ROTA LISTA 
@app.route('/lista')
def lista():
    return render_template('lista.html')
    
# ROTA FORMULÁRIO
@app.route('/formulario')
def formulario():   
    return render_template('formulario.html')

# ROTA CADASTRO
@app.route('/cadastro')
def cadastro(): # Mudei de 'index' para 'cadastro'
    return render_template('cadastro.html')

# Iniciando o servidor
if __name__ == '__main__':
    app.run(debug=True)