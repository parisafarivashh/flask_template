from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional


class SignupForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  last_name = StringField('Last_Name', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired()])
  password =PasswordField('Password', validators=[DataRequired(), Length(min=6 ,message='Select Strong Password')])
  confirm = PasswordField('Confirm your password', validators=[DataRequired(), EqualTo('password', message='password must be match')])
  submit = SubmitField('Submit')   


class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired()])
  password =PasswordField('Password', validators=[DataRequired(), Length(min=6 ,message='Select Strong Password')])
  # confirm = PasswordField('Confirm your password', validators=[DataRequired(), EqualTo('Password', message='password must be match')])
  submit = SubmitField('Submit')

class AddresForm(FlaskForm):
  name = StringField('Adress', validators=[DataRequired()]) 
  submit = SubmitField('Submit')

class ProfileForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  last_name = StringField('Last_Name', validators=[DataRequired()])
  submit = SubmitField('Submit')