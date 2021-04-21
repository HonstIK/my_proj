import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Sharks(db.Model):
    __tablename__ = 'Sharks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    view = db.Column(db.String(100))
    color = db.Column(db.String(100))
    jaw = db.Column(db.String(100))
