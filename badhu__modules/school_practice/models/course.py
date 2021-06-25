from odoo import api, fields, models


class Course(models.Model):
    _name = 'course.details'
    _description = 'This is the course class'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'course_name'

    course_name = fields.Char()
    amount = fields.Integer()
    duration = fields.Integer()
    is_active = fields.Boolean(default=True)
    price_tax = fields.Float(string='Total Tax')
