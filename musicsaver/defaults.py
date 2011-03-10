"""
Application Configuration 
"""


# Database

SQLALCHEMY_DATABASE_URI = 'mysql://root:1z8P472RKF@127.0.0.1/musicsaver'
SQLALCHEMY_POOL_RECYCLE = 1000

# Music Constraints

SONGS_PER_MINUTE = 3
SONGS_PER_HOUR = 25
SONGS_PER_DAY = 200

WARNING_URL = 'http://jamsspace.com/songs/warning.mp3'

MUSIC_CACHE_DIR = '/mp3/'

ALLOWED_SITES = ['jamsspace.com',]
CACHED_SITES = []

USER_BLACKLIST = ['127.0.0.1']

# Migration Fetching Information

CREDS = {
    'jamsspace.com': ('user', 'auth'),
}


INFODB_API_KEY = '8f3afe018b36e90403e7aecdf16215042ecd3fe3dfb3140de8c2e3685a74f357'
