import asyncio
from aiohttp import web


def async_task(request):
    asyncio.sleep(5)
    return None


async def index(request):
    app = request.app
    loop = app.loop
    loop.create_task(async_task(request))
    return web.HTTPOk(body='ok')