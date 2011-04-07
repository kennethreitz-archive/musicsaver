from flaskext.sqlalchemy import SQLAlchemy
from musicsaver import app

__version__ = '0.0.1'

db = SQLAlchemy(app)


class AccessLog(db.Model):
    """The :class:`AccessLog` object is a record of a song being accessed.
    """

    __tablename__ = 'access_logs'

    id = db.Column(db.Integer, primary_key=True)

    origin = db.Column(db.String(80))
    song = db.Column(db.String(800))
    geo = db.Column(db.PickleType)
    success = db.Column(db.Boolean)
    when = db.Column(db.DateTime)
    geo = db.Column(db.PickleType)
