# -*- coding: utf-8 -*-

import hashlib
import os
from datetime import datetime

import requests

from flask import (
	request, session, redirect, url_for,
	abort, render_template, flash, Flask
)

from musicsaver import app
from musicsaver.models import AccessLog

def fetch(url, cache=True):
    """fetches song."""

    # sha1 of url
    hash = hashlib.sha1(url).hexdigest()

    # enter temp directory
    os.chdir(app.config['MUSIC_CACHE_DIR'])


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
    # check valid domain
    

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
        return fetch(url, do_cache)
    else:
        return fetch(app.config['WARNING_URL'])
