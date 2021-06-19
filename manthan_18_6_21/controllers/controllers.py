# -*- coding: utf-8 -*-
# from odoo import http


# class Manthan18621(http.Controller):
#     @http.route('/manthan_18_6_21/manthan_18_6_21/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manthan_18_6_21/manthan_18_6_21/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('manthan_18_6_21.listing', {
#             'root': '/manthan_18_6_21/manthan_18_6_21',
#             'objects': http.request.env['manthan_18_6_21.manthan_18_6_21'].search([]),
#         })

#     @http.route('/manthan_18_6_21/manthan_18_6_21/objects/<model("manthan_18_6_21.manthan_18_6_21"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manthan_18_6_21.object', {
#             'object': obj
#         })
