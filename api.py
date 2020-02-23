# -*- coding: utf-8  -*-
"""
Interface functions to Mediawiki's api.php
"""
#
# (C) redolag 2018
#
# Distributed under the terms of the MIT license.
#
__version__ = '$Id: $'


import urllib
import http


class API:

    def __init__(self, site):
        self.site = site

    def query(prop, **kwargs):
        params = dict(kwargs)
        params['action'] = 'query'
        if not params.has_key('format'): #need JSON format
            params['format'] = 'json'

        return http.HTTP(None).POST('/w/api.php',params)
