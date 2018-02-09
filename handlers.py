import aiohttp
from aiohttp import web


async def async_task(request):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.github.com/events') as resp:
            print(resp.status)
            print(await resp.text())


async def index(request):
    app = request.app
    loop = app.loop
    loop.create_task(async_task(request))
    return web.HTTPOk(body='ok')