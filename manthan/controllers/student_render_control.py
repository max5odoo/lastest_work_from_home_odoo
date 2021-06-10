from odoo.http import request, route
from odoo import http
import json


class Student_render_route(http.Controller):

    @http.route('/studentpage', type='http', auth='public', website=True)
    def student_page(self):
        print(f'\n\n\n\nSUCCESSFULLY ROUTED\n\n\n\n')
        return http.request.render('manthan.student_simple_page')

    @http.route('/studentajax', type='json', method='GET', auth='public')
    def student_ajax(self):
        data = {
            'name': 'manthan'
        }
        return data
