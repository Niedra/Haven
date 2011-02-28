from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from haven.models import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'haven:static')
    config.add_route('root', '/', view='haven.views.root',
                     view_renderer='root.mako')
    return config.make_wsgi_app()


