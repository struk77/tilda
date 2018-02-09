#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'epicwn'

import asyncio
from aiohttp import web
import sys

from handlers import index

import logging

# Enable logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

DEBUG = True


def main(argv):
    loop = asyncio.get_event_loop()
    app = web.Application(loop=loop)
    app.router.add_get('/', index)
    web.run_app(app, host='0.0.0.0', port=8000)


if __name__ == "__main__":
    main(sys.argv[1:])