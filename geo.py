#!/usr/bin/env python
# -*- coding: utf-8 -*-

from musicsaver.packages import pyipinfodb

api = pyipinfodb.IPInfo('8f3afe018b36e90403e7aecdf16215042ecd3fe3dfb3140de8c2e3685a74f357')

print api.GetCity('207.97.227.239')