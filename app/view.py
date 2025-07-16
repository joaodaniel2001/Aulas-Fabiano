from app import app, db
from flask import render_template, url_for, request, redirect
from app.models import Contato
from app.forms import ContatoForm, UserForm, LoginForm, PostForm
from flask_login import login_user, logout_user, current_user

@app.route('/', methods=['GET', 'POST'])
def homepage():
    usuario = 'João'
    idade = 17
    form = LoginForm()
    
    if form.validate_on_submit():
        user = form.login ()
        login_user(user, remember=True)

    context = {
        'usuario':usuario,
        'idade':idade
    }

    return render_template('index.html', context=context, form=form)

# Cadastro
@app.route('/cadastro/', methods=['GET', 'POST'])
def cadastro():
    form = UserForm()
    if form.validate_on_submit():
        user = form.save()
        login_user(user, remember=True)
        return redirect(url_for('homepage'))
    return render_template('cadastro.html', form=form)

# Post
@app.route('/post/novo')
def PostNovo ():
    form = PostForm()
    if form.validate_on_submit():
        form.save(current_user.id)
        return redirect(url_for('homepage'))
    return render_template('cadastro.html', form=form)

# Deslogar
@app.route('/sair/')
def logout ():
    logout_user()
    return redirect(url_for('homepage'))

# Contato
@app.route('/contato/', methods=['GET','POST'])
def contato():
    form = ContatoForm()
    context={}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
    return render_template('contato.html',context=context,form=form)

# Contato Lista
@app.route('/contato/lista/', methods=['GET','POST'])
def contatoLista():
    if request.method=='GET':
        pesquisa=request.args.get('pesquisa','')

    dados = Contato.query.order_by()
    if pesquisa != '':
        dados = dados.filter_by(nome=pesquisa)
    context={'dados': dados.all()}


    return render_template('contatoLista.html',context=context)

# Contato Detalhado
@app.route('/contato/<int:id>')
def contatoDetail(id):
    obj=Contato.query.get(id)
    return render_template('contato_detail.html', obj=obj)