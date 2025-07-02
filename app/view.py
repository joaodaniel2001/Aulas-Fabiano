
from app import app
from flask import render_template, url_for, request
from app.forms import ContatoForm

@app.route('/')
def homepage():
    
    usuario = 'João Daniel'
    idade = 17

    context = {
        'usuario': usuario,
        'idade': idade
    }

    return render_template('index.html', context=context)

@app.route('/contato/', methods=['GET', 'POST'])
def novapagina():
    form = ContatoForm()
    context = {}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        print('GET', pesquisa)
        context.update({'pesquisa':pesquisa})

    if request.method == 'POST':
        pesquisa = request.args.get('pesquisa')
        print('POST', pesquisa)
        context.update({'pesquisa':pesquisa})

    return render_template('contato.html', context=context)
