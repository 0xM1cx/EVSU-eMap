from flask import Flask, render_template, redirect, flash, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, Length, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'kunwariSecretLang'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maps_user.db'
db = SQLAlchemy(app)


class User(db.model):
    __table__ = 'User_Table'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    age = db.Column(db.String(200), nullable=False)
    address_name = db.Column(db.String(200), nullable=False)


class RegistrationForm(FlaskForm):
    First_Name = StringField('First Name', validators=[DataRequired(), Length(min=3, max=100)])
    Last_Name = StringField('Last Name', validators=[DataRequired(), Length(min=3, max=100)])
    Age = StringField('Age', validators=[DataRequired(), Length(min=3, max=100)])
    Address = StringField('Age', validators=[DataRequired(), Length(min=3, max=100)])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


app.route('/registration', methods=['POST', 'GET'])


def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        FirstName = form.First_Name.data
        LastName = form.Last_Name.data
        Age = form.Age.data
        Address = form.Address.data
        new_User = User(First_Name=FirstName, Last_Name=LastName, Age=Age, Address=Address)
        db.session.add(new_User)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('landing'))

    return render_template('index.html', form=form)


app.route('/login', methods=['POST', 'GET'])


def home():
    return render_template('home.html')


app.route('/', methods=['POST', 'GET'])


def landing():
    return render_template('index.html')


app.route

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
