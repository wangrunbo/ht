from flask import render_template, url_for
from flask_mail import Message
from .. import app, mail
from ..model import Setting
from .security import ts
from .decorators import async


def message():
    """
    デフォルト設定
    :return:
    """
    return Message()


def subject(sub):
    """
    メールタイトル
    :param sub:
    :return:
    """
    return f'「{Setting.get("SITE_NAME")}」{sub}'


@async
def send_mail(msg=None):
    """
    メールを送信する
    :param msg:
    :return:
    """
    if msg is None:
        msg = message()

    with app.app_context():
        mail.send(msg)


def send_register_mail(user):
    """
    会員新規登録メール認証
    :param user:
    :return:
    """
    msg = message()

    msg.subject = subject('会員メール認証')
    msg.add_recipient(user.email)
    msg.html = render_template(
        'mail/register.html',
        user=user,
        url=url_for('register.complete', token=ts.dumps(user.secret_key, salt=app.config['TOKEN_SALT']), _external=True)
    )

    send_mail(msg)
