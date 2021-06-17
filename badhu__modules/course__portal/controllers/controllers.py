# -*- coding: utf-8 -*-
# from odoo import http


# class CoursePortal(http.Controller):
#     @http.route('/course__portal/course__portal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/course__portal/course__portal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('course__portal.listing', {
#             'root': '/course__portal/course__portal',
#             'objects': http.request.env['course__portal.course__portal'].search([]),
#         })

#     @http.route('/course__portal/course__portal/objects/<model("course__portal.course__portal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('course__portal.object', {
#             'object': obj
#         })
