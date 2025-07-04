
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
    dados = Contato.query.all()
    print(dados)
    context = {}
    return render_template ('contatoLista.html', context=context)