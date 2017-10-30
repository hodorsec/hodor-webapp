# -*- coding: utf-8 -*-

from hodor import db


class Challenges(db.Model):
    __tablename__= 'challenges'

    # Data variables for each challenge
    id = db.Column(db.String(32), primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(32), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(2048), nullable=False)
    hints = db.Column(db.String(512), nullable=False)

    @staticmethod
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_all():
        return Challenges.query.all()
