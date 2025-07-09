
from app import app, db
from flask import render_template, url_for, request, redirect
from app.forms import ContatoForm
from app.models import Contato

@app.route('/')
def homepage():
    usuario = "João Daniel"
    idade = 17

    context = {
        'usuario': usuario,
        'idade': idade
    }

    return render_template('index.html', context=context)

@app.route ('/contato/', methods = ['GET', 'POST'])
def contato ():
    form = ContatoForm ()
    context = {}
    
    if form.validate_on_submit ():
        form.save ()
        return redirect(url_for('homepage'))
    
    return render_template ('contato.html', context=context, form=form)

@app.route('/contato/lista/')
def contatoLista ():
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa', '')
    dados = Contato.query.order_by('nome')
    if pesquisa != '':
        dados = dados.filter_by (nome=pesquisa)
    context = {'dados': dados.all()}

    for linha in dados:
        print(linha.nome)
        print(linha.email)
        print(linha.assunto)
        print(linha.respondido)
        
    return render_template('contatoLista.html', context=context)

@app.route('/contato/<int:id>')
def contatoDetail (id):
    obj=Contato.query.get(id)
    return render_template('contato_detail.html', obj=obj)