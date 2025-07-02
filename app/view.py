
from app import app
from flask import render_template, url_for, request

@app.route('/')
def homepage():
    
    usuario = 'João Daniel'
    idade = 17

    context = {
        'usuario': usuario,
        'idade': idade
    }

    return render_template('index.html', context=context)

@app.route('/contato/')
def novapagina():
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        print(pesquisa)
    return render_template('contato.html')
