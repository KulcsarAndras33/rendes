# -*- coding: utf-8 -*-
# from odoo import http


# class Rendes(http.Controller):
#     @http.route('/rendes/rendes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rendes/rendes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rendes.listing', {
#             'root': '/rendes/rendes',
#             'objects': http.request.env['rendes.rendes'].search([]),
#         })

#     @http.route('/rendes/rendes/objects/<model("rendes.rendes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rendes.object', {
#             'object': obj
#         })
