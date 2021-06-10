from odoo import api, fields, models


class Professor(models.Model):
    _name = 'professor.details'
    _description = 'This is the professor class'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'first_name'

    first_name = fields.Char()
    last_name = fields.Char()
    mobile_no = fields.Integer(max_length=10)
    address = fields.Text()
    email = fields.Char()
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ], 'Gender', default='male')
    profile_pic = fields.Image()
    dob = fields.Date()
    age = fields.Integer()
