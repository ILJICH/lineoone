# coding: utf-8
"""
Main web server.
"""

from logging import getLogger
from jinja2.environment import Environment
from jinja2.loaders import PackageLoader
from tornado import ioloop
from tornado.web import RedirectHandler, Application, StaticFileHandler

from webserver.handlers.iv_calc import IVCalcHandler

__author__ = 'iljich'


def start_server(port):

    logger = getLogger('lineoone.main')

    logger.info('Rise and shine')

    settings = {
        'jinja2_environment': Environment(
            loader=PackageLoader('webserver', 'templates'))
    }

    application = Application([
        (r'/', RedirectHandler, {'url': r'/iv_calc'}),
        (r'/iv_calc', IVCalcHandler),
        (r'/public/(.*)', StaticFileHandler, {'path': 'public'})
    ], **settings)

    application.listen(port)
    ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    start_server(8888)
