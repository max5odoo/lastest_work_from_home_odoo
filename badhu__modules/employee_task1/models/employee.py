from odoo import api, fields, models
import datetime, time


class Employee(models.Model):
    _name = 'employee.document'
    _description = 'employee description'
    _rec_name = 'employee_task_ids'

    name = fields.Char(required=True)
    employee_task_ids = fields.Many2one('hr.employee', string="Employees")
    employee_doc_name = fields.Char(related="employee_task_ids.name")
    employee_file = fields.Binary(string='Upload File')
    expiry_date = fields.Date(string="Expiry date", required=True, help="Date of Birth")
    state = fields.Selection(
        [('draft', 'Draft'), ('approve', 'Approved'), ('expiry', 'Expired'), ('refuse', 'Refussed')],
        string="emplpoyee status",
        default="draft", compute='document_state', store=True)


    def button_refuse(self):
        for rec in self:
            rec.write({'state': 'refuse'})

    def button_approve(self):
        for rec in self:
            rec.write({'state': 'approve'})

    @api.depends("expiry_date")
    def document_state(self):
        self.state = ''
        for rec in self:
            today_date = datetime.date.today()
            if rec.expiry_date >= today_date:
                rec.state = 'expiry'
            else:
                rec.state = 'draft'
