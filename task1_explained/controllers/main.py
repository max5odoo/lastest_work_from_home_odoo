from odoo import http
from odoo.http import request


class CustomPage(http.Controller):

    @http.route('/shivam', auth='public', website=True)
    def page_shivam(self):
        return request.render("task1_explained.shivam_site_template")

    @http.route('/registration', auth='public', website=True)
    def register_here(self, **kw):
        students = request.env['res.partner'].sudo().search([('is_student', '=', 'student')])
        batches = request.env['batch.details'].sudo().search([])
        courses = request.env['course.details'].sudo().search([])
        professor = request.env['professor.details'].sudo().search([])
        return request.render("task1_explained.register_template_website", {'students': students,
                                                                            'batches': batches,
                                                                            'courses': courses,
                                                                            'professor': professor})

    @http.route('/registration/submit', auth='public', website=True)
    def submit_form(self, **kw):
        print(f"\n\n\nkw - - {kw}\n\n")
        request.env['student.details'].sudo().create(kw)
        return request.render("task1_explained.submit_template_website")