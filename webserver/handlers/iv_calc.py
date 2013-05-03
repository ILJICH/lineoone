# coding: utf-8
"""
Handler to serve IV calculator.
"""

from tornado.web import RequestHandler

__author__ = 'iljich'


class IVCalcHandler(RequestHandler):

    def get(self):
        self.write("It works!")
