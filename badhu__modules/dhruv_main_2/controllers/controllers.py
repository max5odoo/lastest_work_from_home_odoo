# -*- coding: utf-8 -*-
# from odoo import http


# class NewApp2(http.Controller):
#     @http.route('/dhruv_main_2/dhruv_main_2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dhruv_main_2/dhruv_main_2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dhruv_main_2.listing', {
#             'root': '/dhruv_main_2/dhruv_main_2',
#             'objects': http.request.env['dhruv_main_2.dhruv_main_2'].search([]),
#         })

#     @http.route('/dhruv_main_2/dhruv_main_2/objects/<model("dhruv_main_2.dhruv_main_2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dhruv_main_2.object', {
#             'object': obj
#         })\
