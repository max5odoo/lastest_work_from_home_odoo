# -*- coding: utf-8 -*-
# from odoo import http


# class System(http.Controller):
#     @http.route('/system/system/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/system/system/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('system.listing', {
#             'root': '/system/system',
#             'objects': http.request.env['system.system'].search([]),
#         })

#     @http.route('/system/system/objects/<model("system.system"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('system.object', {
#             'object': obj
#         })
