# coding: utf-8
from logging import getLogger
from tornado import ioloop
from tornado.web import RedirectHandler, Application, StaticFileHandler

from webserver.handlers.iv_calc import IVCalcHandler

__author__ = 'iljich'

"""
Main web server.
"""


def start_server(port):

    logger = getLogger('lineoone.main')

    logger.info('Rise and shine')

    application = Application([
        (r'/', RedirectHandler, {'url': r'/iv_calc'}),
        (r'/iv_calc', IVCalcHandler),
        (r'/public/(.*)', StaticFileHandler, {'path': 'public'})
    ])

    application.listen(port)
    ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    start_server(8888)
