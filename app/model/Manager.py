from sqlalchemy.ext.hybrid import hybrid_property
from .. import db, bcrypt


class Manager(db.Model):
    """管理者"""
    __tablename__ = 'managers'

    id = db.Column(db.Integer, primary_key=True)
    _password = db.Column('password', db.String(128), nullable=False)

    note = db.Column(db.Text, nullable=True, server_default=None)
    created = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text('CURRENT_TIMESTAMP'))
    updated = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted = db.Column(db.TIMESTAMP, nullable=True, server_default=None)

    def __repr__(self):
        return f'<Manager {self.id}>'

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = bcrypt.generate_password_hash(value)
