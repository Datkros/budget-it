from aiohttp import web

def build_producer():


    app = web.Application()

    return app


if __name__ == '__main__':
    app = build_producer()
    web.run_app(app, port=8005)