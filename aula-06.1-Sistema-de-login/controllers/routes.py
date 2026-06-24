from flask import render_template, request, redirect, url_for, flash, session
# Importando o Markup Safe (sem ele n dá pra inserir link)
from markupsafe import Markup 
from model.game import listar_games, adicionar_game
from model.database import Game, Console, db, Usuario
# Importando WERKZEUG
from werkzeug.security import generate_password_hash, check_password_hash

def init_app(app):

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/games')
    def games():
        return render_template(
            'games.html',
            game={
                "titulo": "Warframe",
                "ano": 1999,
                "categoria": "RPG"
            },
            jogadores=['Eduardo', 'Ana', 'Guilherme', 'Vitor', 'Antonio']
        )

    @app.route('/consoles')
    def consoles():
        return render_template(
            'consoles.html',
            nome="Nintendo Switch",
            lançamento=1969,
            marca="Nintendo",
            consoles=['PS4', 'Xbox', 'Nintendo Switch', 'PS5', 'PS1']
        )

    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():

        if request.method == 'POST':

            titulo = request.form.get('titulo')
            ano = request.form.get('ano')
            categoria = request.form.get('categoria')

            if titulo and ano and categoria:
                adicionar_game(titulo, ano, categoria)

            return redirect(url_for('cadgames'))

        return render_template(
            'cadgames.html',
            listaGames=listar_games()
        )

    @app.route('/estoque_jogos', methods=['GET', 'POST'])
    def estoque_jogos():

        if request.method == 'POST':

            dados_form = request.form.to_dict()

            newGame = Game(
                titulo=dados_form['titulo'],
                ano=dados_form['ano'],
                categoria=dados_form['categoria'],
                plataforma=dados_form['plataforma'],
                preco=dados_form['preco'],
                quantidade=dados_form['quantidade']
            )

            db.session.add(newGame)
            db.session.commit()

            return redirect(url_for('estoque_jogos'))

        games = Game.query.all()

        return render_template(
            'estoque_jogos.html',
            games=games
        )

    @app.route('/estoque_jogos/delete/<int:id>')
    def deletar_jogo(id):

        game = Game.query.get(id)

        if game:
            db.session.delete(game)
            db.session.commit()

        return redirect(url_for('estoque_jogos'))
    
    
    @app.route('/editar-jogos/<int:id>', methods=['GET', 'POST'])
    def editar_jogos(id):
        # Buscando jogo no banco
        game = Game.query.get(id)
        #Verficando s ea requisição é POST
        if request.method == 'POST':
            # Coletando os dados do formulário
            dados_form = request.form.to_dict()
            # Passando os dados do formulário para o jogo
            game.titulo = dados_form['titulo']
            game.titulo = dados_form['ano']
            game.titulo = dados_form['categoria']
            game.titulo = dados_form['plataforma']
            game.titulo = dados_form['preco']
            game.titulo = dados_form['quantidade']
            # Confirmando as alterações no banco
            db.session.commmit()
            return redirect(url_for('estoque'))
        return render_template('editar-jogos.html', game=game)
    

    @app.route('/estoque_consoles', methods=['GET', 'POST'])
    def estoque_consoles():

        if request.method == 'POST':

            dados_form = request.form.to_dict()

            newConsole = Console(
                nome=dados_form['nome'],
                fabricante=dados_form['fabricante'],
                ano=dados_form['ano'],
                preco=dados_form['preco'],
                quantidade=dados_form['quantidade']
            )

            db.session.add(newConsole)
            db.session.commit()

            return redirect(url_for('estoque_consoles'))

        consoles = Console.query.all()

        return render_template(
            'estoque_consoles.html',
            consoles=consoles
        )

    @app.route('/estoque_consoles/delete/<int:id>')
    def deletar_console(id):

        console = Console.query.get(id)

        if console:
            db.session.delete(console)
            db.session.commit()

        return redirect(url_for('estoque_consoles'))
    
    # Cadastro de Usuario
    
    @app.route('/cadastro', methods=['GET', 'POST'])
    def cadastro(): 
        # Verificando se o metodo é POST
        if request.method == 'POST':
            # Coletando os dados do Formulário
            email = request.form['email']
            senha = request.form['senha']
            # VERIFICANDO SE O USUARIO JÁ EXISTE
            # Buscando o usuário pelo e-mail
            usuario = Usuario.query.filter_by(email=email).first()
            # Verificando s eo usuário possui valor
            if usuario:
                msg = Markup("Usuário já cadastrado. Faça o <a href='/login'>Login</a>")
                flash(msg, 'danger')
                return redirect(url_for('cadastro'))

                
            # GERANDO O HASH DE SENHA (CRIPTOGRAFIA)
            senha_criptografada = generate_password_hash(senha, method='scrypt')
            # Enviando os dados para o Model
            novo_usuario = Usuario(email=email, senha=senha_criptografada)
            # Cadastrando no banco
            db.session.add(novo_usuario)
            db.session.commit()
            # Gerando a mesnsagem de sucesso
            msgCad = Markup("Cadastro realizado com sucesso! Faça o <a href='/login'>Login</a>")
            flash(msgCad, 'success')
            return redirect(url_for('cadastro'))
        return render_template('cadastro.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        #VERIFICANDO SE O METODO É POST
        if request.method == 'POST':
            #COLETANDO OS DADOS DO USUÁRIO
            email = request.form['email']
            senha = request.form['senha']
            #BUSCANDO O USUARIO NO BANCO
            usuario = Usuario.query.filter_by(email=email).first()
            # SE O USUARIO EXISTIR
            if usuario:
                #VERIFICANDO A SENHA (hash)
                if check_password_hash(usuario.senha, senha):
                    #AQUI SERA CRIADO A SESSÃO
                    session['usuario_id'] = usuario.id
                    session['usuario_email'] = usuario.email
                    # Mensagemde feedback
                    msgLogin = "Você foi autenticado com succeso! Bem-vindo!"
                    flash(msgLogin, 'sucess')
                    return redirect(url_for('home'))
                
                # CASO SENHA INCORRETA
                else:
                    flash('Falha nno login. Verifique os dados e tente novamente!', 'danger')
            
            # SE O USUARIO N FOR ENCONTRADO
            else:
                flash('O usuário informado não existe!', 'danger')
                return redirect(url_for('login'))
            
        return render_template('login.html')