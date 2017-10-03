from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField(
        label='ユーザー名',
        validators=[DataRequired(message='ユーザー名を入力してください')]
    )
    password = PasswordField(
        label='パスワード',
        validators=[DataRequired(message='パスワードを入力してください')]
    )
