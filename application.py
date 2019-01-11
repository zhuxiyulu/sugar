#!/usr/bin/env python
# coding=utf-8

import tornado.web
import os
from urls import url

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "templates/static"),
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "xsrf_cookies": False,
}

application = tornado.web.Application(
    handlers=url,
    **settings
)