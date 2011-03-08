from flaskext.sqlalchemy import SQLAlchemy
from musicsaver import app

__version__ = '0.0.1'

db = SQLAlchemy(app)


class URL(db.Model):
    """The :class:`URL` object is a sanitized DTA2800 migration log.
    """

    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    song = db.Column(db.String(800))
    active = db.Column(db.Boolean)
    referrer = db.Column(db.String(800))

    def get_song(self):
        # return song
        pass

    def check_kosher(self):
        #check agaisnt config
        #save self
        # return true/false
        pass

    def __init__(self):
        self.active = True

    def __repr__(self):
        return '<url %r>' % self.id


class AccessLog(db.Model):
    """The :class:`AccessLog` object is a record of a song being accessed.
    """

    __tablename__ = 'access_logs'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    origin = db.Column(db.String(80))
    song = db.Column(db.String(800))



