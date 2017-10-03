from .. import db


class Prefecture(db.Model):
    """都道府県"""
    __tablename__ = 'prefectures'

    id = db.Column(db.SmallInteger, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    sort = db.Column(db.Integer, nullable=False, unique=True)
    created = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text('CURRENT_TIMESTAMP'))
    updated = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted = db.Column(db.TIMESTAMP, nullable=True, server_default=None)

    def __init__(self, name):
        self.name = name
        self.sort = 0  # TODO

    def __repr__(self):
        return f'<Prefecture {self.name}>'
