from odoo import api, fields, models
from datetime import date

# class ContactInherite(models.Model):
#     _inherit = "res.partner"
#     # _order = 'id desc'
#     is_professor = fields.Boolean(string="Is Professor")


class Professor(models.Model):
    _name = 'professor.details'
    _rec_name = 'professor_name'
    _description = "Professor"
    # _inherits = {'student.details': 'his_students'}

    professor_name = fields.Many2one('res.partner', string='Professor')
    photo = fields.Image(related='professor_name.image_1920', string="Photo")
    his_students = fields.One2many('student.details', 'his_professor', string="Students under")
    mobile_no = fields.Char(related='professor_name.phone', string="Mobile no.")
    email = fields.Char(related='professor_name.email', string="Email.")

