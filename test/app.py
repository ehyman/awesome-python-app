#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'Hyman Shi'

''' asyncio app test 
'''

import logging;logging.basicConfig(level=logging.INFO)
import time, json, os, asyncio

from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '0.0.0.0', 8000)
    logging.info('server start at http://0.0.0.0:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
