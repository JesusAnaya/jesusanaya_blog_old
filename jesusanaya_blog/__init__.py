from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models.meta import (
    DBSession,
    Base,
)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    config.add_route('home', '/')
    config.add_route('blog', '/blog/{id:\d+}/{slug}')
    config.add_route('blog_action', '/blog/{action}')
    config.add_route('auth', '/sign/{action}')

    config.scan()
    return config.make_wsgi_app()


__version__ = '0.0.1'
