from aiohttp.web import Application

from .views.healthcheck import HealthcheckView

def initialize_routes(app: Application, container):
    healthcheck_view = HealthcheckView(container=container)
    app.router.add_get('/api-status', healthcheck_view.get_status)