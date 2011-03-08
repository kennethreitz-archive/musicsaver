#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os

from flaskext.script import Manager
from sqlalchemy.ext.serializer import loads, dumps

from musicsaver import app
from musicsaver.models import db


manager = Manager(app)

app.test_request_context('/').push()


@manager.command
def syncdb():
	db.create_all()


@manager.command
def dbname(logs=False):
	"""List DB Name in use."""

	print app.config['SQLALCHEMY_DATABASE_URI']


if __name__ == "__main__":
	manager.run()
