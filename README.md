# Projeto FLASK


## Sumário

- [Pasta .venv](#pasta-.venv)
- [Bibliotecas Flask](#bibliotecas-flask)
- [Comandos](#comandos)
- [Estrutura básica](#estrutura-básica)
- [Segurança .env](#segurança-env)
- [Bibliotecas de segurança](#bibliotecas-de-segurança)

<br>

### **OBS:** Antes de começar o projeto **JAMAIS** esqueça que o local para dar Run e Debug é **APENAS** o ***main.py***

<br>

## Pasta **.venv**

<p>1. Instalação da pasta <b>.venv</b></p>

```bash
python -m venv .venv
```

<br>

<p>2. Ativação no terminal</p>

- Abra o **Command Prompt**
- Reabra o Terminal

```bash
.venv\Scripts\activate
```

<br>

## Bibliotecas Flask

- **Flask:** micro framework web para Python.
```bash
pip install flask
```

- **Flask SQLAlchemy:** permite a manipulação de bancos de dados com um ORM.
```bash
pip install Flask-SQLAlchemy
```

- **Flask Migrate:** utiliza Alembic para gerenciar migrações do banco de dados.

```bash
pip install Flask-Migrate
```

- **Flask-WTF:** integra o WTForms ao Flask, facilitando a criação de formulários HTML.

```bash 
pip install Flask-WTF
```

<br>


<br>

## Comandos

- Inicializar a pasta de **migrações**:

```bash
flask db init
```

<br>

- Cria uma migração com uma nova **mensagem**:
```bash
flask db migrate -m "mensagem"
```

<br>

- Aplica as migrações ao **banco de dados**:

```bash
flask db upgrade
```

<br>

## Estrutura básica

- Crie uma arquivo **main.py** e escreva:

```bash
from flask import Flask

app = Flask (__name__)
@app.route ('/')
def homepage ():
    return 'Minha primeira página Flask'

if __name__ == '__main__':
    app.run (debug=True)

```

- Inicie o código, e no **terminal**, copie o código **http** e cole no navegador que seu código flask funcionará:
```bash
- Running on http://127.0.0.1:5000
```

## Segurança **.env**

- **Instalação do arquivo .env:** no terminal escreva o comando abaixo.

```bash
pip install python-dotenv
```

- Após isso, fora da pasta app, crie um arquivo chamado **.env**. Neste arquivo, escreva o seguinte:

```bash
DATABASE_URI = 'sqlite:///database.db'
SECRET_KEY = 'senha'
```

- Depois de baixar as bibliotecas de segurança **(login & bcrypt)**, crie um arquivo chamado ***create_secret.py***, e dentro dele escreva:

```bash
import secrets

sk = secrets.token_hex(24) # quantidade de caracteres

print (sk)
```

- Inicialize o arquivo e copie o conteúdo do terminal, após isso, vá até o arquivo  ***.env*** e cole a senha no **SECRET_KEY**:

```bash
DATABASE_URI = 'sqlite:///database.db'
SECRET_KEY = 'a50ee2b080c8ca02dd7d4ca3c1316d614dbf04578a7a5d19' # <-- Aqui
```

## Bibliotecas de segurança                                                                                                                                         

- **Flask login:** 

```bash
pip install flask-login
```

- **Flask bcrypt:** 

```bash
pip install flask-bcrypt
```

- **Email validator:** 

```bash
pip install email-validator
```
