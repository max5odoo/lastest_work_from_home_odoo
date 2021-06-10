# -*- coding: utf-8 -*-
# from odoo import http


# class CalendarTask(http.Controller):
#     @http.route('/calendar_task/calendar_task/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/calendar_task/calendar_task/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('calendar_task.listing', {
#             'root': '/calendar_task/calendar_task',
#             'objects': http.request.env['calendar_task.calendar_task'].search([]),
#         })

#     @http.route('/calendar_task/calendar_task/objects/<model("calendar_task.calendar_task"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('calendar_task.object', {
#             'object': obj
#         })
