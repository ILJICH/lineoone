# coding: utf-8
"""
Handler to serve IV calculator.
"""

from tornado.web import RequestHandler

__author__ = 'iljich'


class IVCalcHandler(RequestHandler):

    def get(self):
        env = self.application.settings['jinja2_environment']
        self.finish(env.get_template('iv_calc/main.jinja2').render())
