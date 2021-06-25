from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Registration(models.Model):
    _name = 'registrations.details'
    _description = 'Registrations details'
    _rec_name = 'student'

    student = fields.Many2one('student.details', string="Student", required=True)
    batch_id = fields.Many2one('batch.details', string="Batches")
    # course_ids = fields.One2many(related="batch_id.course_ids",string="Course")
    course_ids = fields.Many2many('course.details', 'registration_course_rel', 'reg_id', 'course_id', string="Course")
    select_course = fields.Many2one(comodel_name='course.details')


    # course_tobe_print = fields.Many2many('batch.details', 'course_from_batch', 'batch', 'courses', string="Courses")
    # c_ids = fields.Char(related='course_ids.course_name', string='Courses')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done')
    ], string="Status", readonly=True, default='draft')

    currency_id = fields.Many2one(related='course_ids.currency_id', string="Currency", readonly=True,
                                  default=lambda self: self.env['res.currency'].browse([20]))
    total_fees = fields.Monetary(related="batch_id.total_fees", string="Total fees")

    _sql_constraints = [
        ('name_unique', 'unique(student)', "There cannot be multiple Registration from same student !"),
    ]

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state= 'done'

    @api.onchange('batch_id')
    def onchange_batch_id(self):
        for rec in self:
            rec.course_ids = rec.batch_id.course_ids

    def graph_view(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'registrations.details',
            'view_mode': 'graph',
        }
