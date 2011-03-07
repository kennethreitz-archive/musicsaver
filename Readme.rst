Music Saver
===========

Saves your Public MP3s.

Music Request Process:

- user opens music page
- php registers temporary url for user, passes it to players
- players request mp3 from this app
- app checks database for constraints
- if kosher, stream mp3 to user, logs info
    - grabs mp3 from server (http authed)
    - responds with it (slowly if possible)


Notes:
------

- ``user_id`` is sha1 of ip address
- Block known scapers

Disable access for known referrals and such.

Configuration:
--------------

    SONGS_PER_MINUTE = 3
    SONGS_PER_HOUR = 16
    SONGS_PER_DAY = 180
    URL_EXPIRES_MINUTES = 15
    
    
Routes
------

- `/get?song=<url-for-song>`
    Returns url for player to use. Good for 15 minutes?
- `/get?song=<url-for-song>`
    Returns url for player to use. Good for 15 minutes?
    
