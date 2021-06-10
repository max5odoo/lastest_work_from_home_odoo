from odoo import api, fields, models


class Course(models.Model):
    _name = 'course.details'
    _description = 'This is the course class'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    course_name = fields.Char()
    amount = fields.Integer()
    duration = fields.Integer()
    is_active = fields.Boolean(default=True)
