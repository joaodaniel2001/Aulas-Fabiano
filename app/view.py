
from app import app, db
from flask import render_template, url_for, request
from app.forms import ContatoForm

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
    
    return render_template ('contato.html', context=context, form=form)
