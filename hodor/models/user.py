# -*- coding: utf-8 -*-

from hodor import db
from sqlalchemy import inspect
from sqlalchemy_utils import PasswordType


class User(db.Model):
    __tablename__ = 'users'

    # Values entered by the user
    username = db.Column(db.String(32), primary_key=True, nullable=False)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    country = db.Column(db.String(64))
    avatar_url = db.Column(db.String(256))
    '''PasswordType is an awesome function. To check for passwords later,
        you can just do user['password'] == 'plaintext' for a boolean response.'''
    password = db.Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated=['md5_crypt']
    ), nullable=False)

    # Platform values
    disabled = db.Column(db.Boolean, default=False)
    verified_account = db.Column(db.Boolean, default=False)
    verification_code = db.Column(db.String(32), nullable=False)

    def __unicode__(self):
        return unicode(self.username)

    def save(self):
        print type(self)
        print self.email
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()

    def get_all_dict(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<User: {}>".format(self.name)
