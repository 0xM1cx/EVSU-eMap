from flask import Flask, render_template, redirect, flash, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, Length, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'kunwariSecretLang'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maps_user.db'
# db = SQLAlchemy(app)


# class User(db.model):
#     __table__ = 'User_Table'
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(200), nullable=False)
#     username = db.Column(db.String(200), nullable=False)
#     password = db.Column(db.String(200), nullable=False)


# class RegistrationForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Length(min=3, max=100)])
#     username = StringField('Username', validators=[DataRequired(), Length(min=3, max=100)])
#     password = StringField('Password', validators=[DataRequired(), Length(min=3, max=100)])


# class LoginForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('Log In')


# app.route('/', methods=['POST'])
# def register():
#     form = RegistrationForm()

#     if form.validate_on_submit():
#        pass

#     return render_template('login.html', form=form)


@app.route('/')
def home():
    return render_template('login.html')

@app.route('/home')
def landing():
    return render_template('main.html')

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
