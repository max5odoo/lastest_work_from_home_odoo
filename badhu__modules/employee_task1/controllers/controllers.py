# -*- coding: utf-8 -*-
# from odoo import http


# class EmployeeTask1(http.Controller):
#     @http.route('/employee_task1/employee_task1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_task1/employee_task1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_task1.listing', {
#             'root': '/employee_task1/employee_task1',
#             'objects': http.request.env['employee_task1.employee_task1'].search([]),
#         })

#     @http.route('/employee_task1/employee_task1/objects/<model("employee_task1.employee_task1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_task1.object', {
#             'object': obj
#         })
