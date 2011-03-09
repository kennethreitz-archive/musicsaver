# -*- coding: utf-8 -*-

from datetime import datetime

import requests

from flask import (
	request, session, redirect, url_for,
	abort, render_template, flash, Flask
)

from musicsaver import app
from musicsaver.models import AccessLog



def store(object):
    """Stores Model instance in database permanently."""

    db.session.add(object)
    db.session.commit()


@app.route('/get', methods=['GET'])
def get_song():
    """Receives song."""

    url = request.args.get('p', app.config['WARNING_URL'])
    r = requests.get(url)
    
    return r.content
