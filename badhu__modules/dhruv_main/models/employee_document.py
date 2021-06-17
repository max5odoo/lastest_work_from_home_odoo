from odoo import models, fields, api
import datetime


class EmployeeDoc(models.Model):
    _name = "employee.document"
    _rec_name = 'employee'

    name = fields.Char()
    file = fields.Binary()
    expiry_date = fields.Date(required=True)
    employee = fields.Many2one('hr.employee', String="Employee Name")
    image_filename = fields.Char(related="employee.name")
    state = fields.Selection(
        [('draft', 'Draft'), ('approved', 'Approved'), ('expired', 'Expired'), ('refused', 'Refused')], default='draft', compute="compute_state", store=True)

    def action_approve(self):
        for rec in self:
            print("staus changed to 'approved'.")
            rec.write({'state': 'approved'})

    def action_refuse(self):
        for rec in self:
            # if rec.state == 'approved':
            print("staus changed to 'refused'.")
            rec.write({'state': 'refused'})

    @api.depends('expiry_date')
    def compute_state(self):
        self.state = ''
        for rec in self:
            today_date = datetime.date.today()
            if rec.expiry_date >= today_date:
                # print("\n\n\n expired. \n\n\n")
                rec.state = 'expired'


class EmployeeUpdate(models.Model):
    _inherit = 'hr.employee'
    doc_cnt = fields.Integer('Docs', compute='get_employee_doc_cnt')

    def get_employee_doc_cnt(self):
        self.doc_cnt = self.env['employee.document'].search_count(
            [('employee', '=', self.id)])

    def action_docs(self):
        # self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Employee Doc tree view',
            'domain': [('employee', '=', self.id)],
            'view_mode': 'tree,form',
            'res_model': 'employee.document',
        }
