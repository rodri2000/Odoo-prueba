# -*- coding: utf-8 -*-
from odoo import http

# class Retofinal(http.Controller):
#     @http.route('/retofinal/retofinal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/retofinal/retofinal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('retofinal.listing', {
#             'root': '/retofinal/retofinal',
#             'objects': http.request.env['retofinal.retofinal'].search([]),
#         })

#     @http.route('/retofinal/retofinal/objects/<model("retofinal.retofinal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('retofinal.object', {
#             'object': obj
#         })