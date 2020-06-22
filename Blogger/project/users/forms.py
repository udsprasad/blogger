from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,ValidationError
from wtforms.validators import DataRequired,Email,EqualTo,Length
from project.users.models import User



class Registerform(FlaskForm):

    email=StringField("Email",validators=[DataRequired(message='Required'),Email('Please enter email')])
    username=StringField('Username',validators=[DataRequired(message='Required'),Length(min=5,max=10,message='username should be in between 5 to 10 Characters')])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=8,message='password must be more than 8 Character'),EqualTo('password_confirm',message='Password must match')])
    password_confirm=PasswordField('Confirm Password',validators=[DataRequired()])
    submit=SubmitField('Register!')

    def validate_email(self,email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Email has already registered')

    def validate_username(self,username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('Username has already registered')
