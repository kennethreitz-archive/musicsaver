#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    musicsaver.core
    ~~~~~~~~~~~~~~~

    This module implements the central application.
"""

from flask import Flask


app = Flask(__name__)

# CONFIGURATION
app.config.from_object('musicsaver.defaults')


try:
	# load from local environment.
	app.config.from_envvar('MUSICSAVER_SETTINGS')
except RuntimeError:
	pass


# Time for views

import musicsaver.views

if __name__ == '__main__':
	app.run()
