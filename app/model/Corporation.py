from sqlalchemy.ext.hybrid import hybrid_property
from .. import db, bcrypt


class Corporation(db.Model):
    """法人"""
    __tablename__ = 'corporations'

    id = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.String(12), unique=True, nullable=False)
    _password = db.Column('password', db.String(128), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    target_email = db.Column(db.String(100), nullable=True)
    secret_key = db.Column(db.String(255), nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    postcode = db.Column(db.String(7), nullable=False)
    prefecture_id = db.Column(db.SmallInteger, db.ForeignKey('prefectures.id'), nullable=False)
    address = db.Column(db.Text, nullable=False)
    tel = db.Column(db.String(11), nullable=False)
    representative = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    corporation_status_id = db.Column(db.SmallInteger, db.ForeignKey('corporation_statuses.id'), nullable=False)

    note = db.Column(db.Text, nullable=True, server_default=None)
    created = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text('CURRENT_TIMESTAMP'))
    updated = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    modifier_id = db.Column(db.Integer, db.ForeignKey('managers.id'), nullable=True, server_default=None)

    prefecture = db.relationship('Prefecture', backref='corporations')
    corporation_status = db.relationship('CorporationStatus', backref='corporations')
    modifier = db.relationship('Manager', backref='modified_corporations')

    def __repr__(self):
        return f'<Corporation {self.name}>'

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = bcrypt.generate_password_hash(value)
