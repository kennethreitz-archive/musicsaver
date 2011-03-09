"""
Application Configuration 
"""


# Database

# SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'


# Music Constraints

SONGS_PER_MINUTE = 3
SONGS_PER_HOUR = 16
SONGS_PER_DAY = 180
URL_EXPIRES_MINUTES = 15

WARNING_URL = 'http://jamsspace.com/songs/warning.mp3'

MUSIC_CACHE_DIR = '/tmp/'

ALLOWED_SITES = ['jamsspace.com',]
CACHED_SITES = ['',]

# Migration Fetching Information

CREDS = {
    'jamsspace.com': ('user', 'auth'),
}


