from flask import Blueprint, render_template, redirect, url_for
from app.form.LoginForm import LoginForm

home = Blueprint('home', __name__)


@home.route('/')
def index():
    # 做些处理
    return render_template('index.html')


@home.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():

        return redirect(url_for('home.index'))

    return render_template('login.html', form=login_form)
