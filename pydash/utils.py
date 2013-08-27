#coding:utf-8
import os
from tornado import httpserver,ioloop,web,wsgi,autoreload
from django.core.handlers import wsgi as django_wsgi

def start_server(options):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pydash.django_settings")
    import pydash.django_settings
    pydash.django_settings.TEMPLATE_DIRS = (options['template_path'],)
    app = web.Application([
                    (r"/static/(.*)", web.StaticFileHandler, {"path":options['static_path']}),
                    ('.*', web.FallbackHandler, dict(fallback=wsgi.WSGIContainer(django_wsgi.WSGIHandler()))),
                    ])
    server = httpserver.HTTPServer(app)
    server.listen(options['port'])
    loop=ioloop.IOLoop.instance()
    autoreload.start(loop)
    loop.start()
    