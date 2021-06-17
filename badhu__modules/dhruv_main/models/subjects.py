from odoo import models, fields, api


class SubjectLine(models.Model):
    _name = "school.subject.line"
    _description = 'Subject Line'
    _rec_name = 'sub_name'
    _order = 'sub_name'
    # _inherit = 'school.professor.detail'

    sub_name = fields.Char(string='Subject Name', required=True)
    sub_desc = fields.Char(string='Subject Desc.')
    student_id = fields.Many2one(
        'school.professor.detail', string='Professor')
