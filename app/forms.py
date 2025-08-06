
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from flask_bcrypt import Bcrypt

bcrypt=Bcrypt()

from app import db, Bcrypt
from app.models import Contato, User, Post

class UserForm (FlaskForm):
    nome = StringField ('Nome', validators=[DataRequired()])
    sobrenome = StringField ('Sobrenome', validators=[DataRequired()])
    email = StringField ('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirmacao_senha = PasswordField('Confirme sua senha', validators=[DataRequired(), EqualTo('senha')])
    btnSubmit = SubmitField('Cadastrar')

    def validade_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('E-mail já cadastrado.')

    def save (self):
        senha = bcrypt.generate_password_hash(self.senha.data.encode('utf-8'))
        user = User (
            nome = self.nome.data,
            sobrenome = self.sobrenome.data,
            email = self.email.data,
            senha = senha.decode('utf-8')
        )

        db.session.add(user)
        db.session.commit()
        return (user)
    
class LoginForm (FlaskForm):
    email = StringField ('E-mail', validators=[DataRequired(),Email()])
    senha = PasswordField ('Senha', validators=[DataRequired()])
    btnSubmit = SubmitField('Login')

    def login (self):
        # Recuperar o usuário do E-Mail
        user = User.query.filter_by (email=self.email.data).first()

        # Verificar se a senha é válida
        if user:
            if bcrypt.check_password_hash (user.senha, self.senha.data.encode ('utf-8')):
                # Retorna o usuário
                return user
            else:
                raise Exception ('Senha incorreta!')
            
        else:
            raise Exception ('Usuário não encontrado!')

class ContatoForm (FlaskForm):
    nome = StringField('Nome', validators = [DataRequired()])
    email = StringField('E-Mail', validators = [DataRequired(), Email()])
    assunto = StringField('Assunto', validators = [DataRequired()])
    mensagem = StringField('Mensagem', validators = [DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save (self):
        contato = Contato (
            nome = self.nome.data,
            email = self.email.data,
            assunto = self.assunto.data,
            mensagem = self.mensagem.data
        )

        db.session.add(contato)
        db.session.commit()
        
class PostForm (FlaskForm):
    mensagem = StringField ('Mensagem', validators=[DataRequired()])
    btnSubmit = SubmitField ('Enviar')

    def save (self, user_id):
        post = Post (
            mensagem = self.mensagem.data,
            user_id = user_id
        )

        db.session.add(post)
        db.session.commit()
        
        return post
    
class PostComentarioForm(FlaskForm):
    mensagem = StringField('Mensagem', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self, user_id, post_id):
        comentario = Post (
            mensagem=self.mensagem.data,
            user_id=user_id,
            post_id=post_id
        )

        db.session.add(comentario)
        db.session.commit()