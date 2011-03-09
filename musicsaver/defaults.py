"""
Application Configuration 
"""


# Database

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
SQLALCHEMY_POOL_RECYCLE = 1000

# Music Constraints

SONGS_PER_MINUTE = 3
SONGS_PER_HOUR = 16
SONGS_PER_DAY = 180

WARNING_URL = 'http://jamsspace.com/songs/warning.mp3'

MUSIC_CACHE_DIR = '/tmp/'

ALLOWED_SITES = ['jamsspace.com',]
CACHED_SITES = ['',]

USER_BLACKLIST = ['']

# Migration Fetching Information

CREDS = {
    'jamsspace.com': ('user', 'auth'),
}


INFODB_API_KEY = '8f3afe018b36e90403e7aecdf16215042ecd3fe3dfb3140de8c2e3685a74f357'
