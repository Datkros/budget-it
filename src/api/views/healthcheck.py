from aiohttp import web
from common.container import ServiceContainer

class HealthcheckView:
    def __init__(self, container: ServiceContainer):
        self.container = container

    async def get_status(self, request: web.Request):
        return web.json_response({"message": "API is healthy"}, status=web.HTTPOk.status_code)
