# -*- coding: utf-8 -*-
# from odoo import http


# class NewApp(http.Controller):
#     @http.route('/dhruv_main/dhruv_main/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dhruv_main/dhruv_main/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dhruv_main.listing', {
#             'root': '/dhruv_main/dhruv_main',
#             'objects': http.request.env['dhruv_main.dhruv_main'].search([]),
#         })

#     @http.route('/dhruv_main/dhruv_main/objects/<model("dhruv_main.dhruv_main"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dhruv_main.object', {
#             'object': obj
#         })
