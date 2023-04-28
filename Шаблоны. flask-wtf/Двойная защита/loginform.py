from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    astronaut_identifier = StringField('Id астронавта', validators=[DataRequired()])
    astronaut_password = PasswordField('пароль астронавта', validators=[DataRequired()])
    captain_identifier = StringField('Id капитана', validators=[DataRequired()])
    captain_password = PasswordField('пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')
