#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os

from flaskext.script import Manager
from sqlalchemy.ext.serializer import loads, dumps

from musicsaver import app
from musicsaver.models import db, AccessLog
from musicsaver.packages import pyipinfodb


manager = Manager(app)

app.test_request_context('/').push()


@manager.command
def syncdb():
	db.create_all()


@manager.command
def dbname(logs=False):
	"""List DB Name in use."""

	print app.config['SQLALCHEMY_DATABASE_URI']


@manager.command
def geo_sync():
    """Add geo information to all logged requests."""

    api = pyipinfodb.IPInfo(app.config['INFODB_API_KEY'])

    logs = AccessLog.query.all()

    for log in logs:

        print log.id,

        log.geo = api.GetCity(log.origin)
        db.session.add(log)
        db.session.commit()

        print '.'



if __name__ == "__main__":
	manager.run()
