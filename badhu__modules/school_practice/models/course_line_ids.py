from odoo import api, fields, models


class Course_lINE(models.Model):
    _name = 'course.line'
    _description = 'This is the course class'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'course_name'

    course_id = fields.Many2one('course.details')
    course_name = fields.Char(related='course_id.course_name')
    amount = fields.Integer(related='course_id.amount')
    duration = fields.Integer(related='course_id.duration')
    prices_tax = fields.Float(related='course_id.price_tax')
    student_id = fields.Many2one('student.details')
