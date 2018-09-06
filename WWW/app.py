#! /usr/bin/env python3
# -*- coding:utf-8 -*-
'''
async web application
'''
import logging; logging.basicConfig(level=logging.INFO)

import asyncio,os,time,json
from datetime import datetime

from aiohttp import web
from jinja2 import Environment,FileSystemLoader


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = await loop.create_server(app._make_handler(),'127.0.0.1',9001)
    logging.info('server start...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()




