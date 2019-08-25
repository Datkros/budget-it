from aiohttp import web
from api.routes import initialize_routes
from common.container import ServiceContainer

def build_api():


    app = web.Application()

    container = ServiceContainer()

    initialize_routes(app, container)

    return app


if __name__ == '__main__':
    app = build_api()
    web.run_app(app, port=8005)