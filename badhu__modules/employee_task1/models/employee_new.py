from odoo import models, fields
import webbrowser



class Employee_new(models.Model):
    _inherit = "hr.employee"

    total_employee = fields.Integer(string='total professor', compute='total_employeess')

    def total_employeess(self):
        count = self.env['employee.document'].search_count([('employee_task_ids', '=', self.name)])
        self.total_employee = count



    def doc_button(self):

        for rec in self:
            name = rec.env['employee.document'].search([('employee_task_ids', '=', self.name)])

            if name:
                return {
                    'name': 'employee',

                    'view_mode': 'tree,form',

                    'res_model': 'employee.document',

                    'domain': [('employee_task_ids', '=', self.name)],
                    'context': {'search_default_employee_task_ids': self.id},

                    'type': 'ir.actions.act_window',
                    # this is predefined in odoo for redirection purpose aa fixed hoyy hamesha
                }

            else:

                return {
                    'name': 'employee',

                    'view_mode': 'form',

                    'res_model': 'employee.document',

                    'type': 'ir.actions.act_window',
                    # this is predefined in odoo for redirection purpose aa fixed hoyy hamesha
                }

    # for redirecting to youtube using webbrowser (button)
    def youtube_button(self):
        return webbrowser.open_new_tab('https://www.youtube.com/')
