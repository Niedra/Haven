from pyramid.config import Configurator
from pyramid_beaker import session_factory_from_settings
from sqlalchemy import engine_from_config

from haven.handlers import add_handlers
from haven.models import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    session_factory = session_factory_from_settings(settings)
    config = Configurator(settings=settings)
    config.set_session_factory(session_factory)
    config.include('pyramid_handlers')
    config.include(add_handlers)
    config.scan('haven.models') # Import models
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    config.add_static_view('static', 'haven:static')
    return config.make_wsgi_app()