from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from haven.handlers import add_handlers
from haven.models import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_handlers')
    config.include(add_handlers)
    config.scan('haven.models') # Import models
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    config.add_static_view('static', 'haven:static')
    return config.make_wsgi_app()