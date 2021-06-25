# -*- coding: utf-8 -*-
# from odoo import http


# class Utsav-test(http.Controller):
#     @http.route('/utsav-test/utsav-test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/utsav-test/utsav-test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('utsav-test.listing', {
#             'root': '/utsav-test/utsav-test',
#             'objects': http.request.env['utsav-test.utsav-test'].search([]),
#         })

#     @http.route('/utsav-test/utsav-test/objects/<model("utsav-test.utsav-test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('utsav-test.object', {
#             'object': obj
#         })
