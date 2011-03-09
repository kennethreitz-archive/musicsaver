# -*- coding: utf-8 -*-

import hashlib
import os
from datetime import datetime, timedelta


import requests

from flask import (
	request, session, redirect, url_for,
	abort, render_template, flash, Flask
)

from musicsaver import app
from musicsaver.models import AccessLog, db
from sqlalchemy.sql import between


def log_request(request, successful):
    """Records given request."""

    log = AccessLog()
    log.origin = request.remote_addr
    log.when = datetime.now()
    log.success = successful
    log.song = request.args.get('p', None)

    store(log)


def fetch(url, cache=True):
    """fetches song."""

    # sha1 of url
    hash = hashlib.sha1(url).hexdigest()

    # enter temp directory
    os.chdir(app.config['MUSIC_CACHE_DIR'])

    # check cache first
    if os.path.exists(hash):
        with open(hash, 'rb') as f:
            return f.read()
    else:
        r = requests.get(url)
        
        if cache:
            with open(hash, 'wb') as f:
                f.write(r.content)

        return r.content


def kosher_request(request):

    url = request.args.get('p', app.config['WARNING_URL'])

    # check blacklist
    if request.remote_addr in app.config['USER_BLACKLIST']:
        return False

    # check if allowed site
    if not any([s in url for s in app.config['ALLOWED_SITES']]):
        return False


    #
    # TIME SENSITIVE CHECKING PER IP
    #

    set = AccessLog.query.filter_by(origin=request.remote_addr)

    now = datetime.now()

    ago_minute = now - timedelta(minutes=1)
    ago_hour = now - timedelta(hours=1)
    ago_day = now - timedelta(days=1)

    past_minute = len(set.filter(between(AccessLog.when, ago_minute, now)).all())
    past_hour = len(set.filter(between(AccessLog.when, ago_hour, now)).all())
    past_day = len(set.filter(between(AccessLog.when, ago_day, now)).all())

    if past_minute > app.config['SONGS_PER_MINUTE']:
        return False

    if past_hour > app.config['SONGS_PER_HOUR']:
        return False

    if past_day > app.config['SONGS_PER_DAY']:
        return False


    return True


def store(object):
    """Stores Model instance in database permanently."""

    db.session.add(object)
    db.session.commit()


@app.route('/get', methods=['GET'])
def get_song():
    """Receives song."""

    url = request.args.get('p', app.config['WARNING_URL'])
    do_cache = any([s in url for s in app.config['CACHED_SITES']])

    if kosher_request(request):
        log_request(request, successful=True)
        return fetch(url, do_cache)
    else:
        log_request(request, successful=False)
        return fetch(app.config['WARNING_URL'])
