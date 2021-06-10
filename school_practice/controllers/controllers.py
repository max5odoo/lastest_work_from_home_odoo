# -*- coding: utf-8 -*-
# from odoo import http


# class SchoolPractice(http.Controller):
#     @http.route('/school_practice/school_practice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school_practice/school_practice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('school_practice.listing', {
#             'root': '/school_practice/school_practice',
#             'objects': http.request.env['school_practice.school_practice'].search([]),
#         })

#     @http.route('/school_practice/school_practice/objects/<model("school_practice.school_practice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school_practice.object', {
#             'object': obj
#         })
