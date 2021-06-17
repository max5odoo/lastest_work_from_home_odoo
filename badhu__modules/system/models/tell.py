from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.exceptions import ValidationError


class Tell(models.Model):
    _name = 'tell.tell'
    _description = 'tell description'
    _inherit = ['website.published.mixin', 'mail.thread', 'mail.activity.mixin']

    name = fields.Char('name', required=True)
    address = fields.Char('address')
    rollno = fields.Integer('Roll No.')
    phoneno = fields.Char('mobile')
    male = fields.Boolean()
    female = fields.Boolean()
    company_name = fields.Char("Company Name", placeholder="enter the comapny name")
    dob = fields.Date(string="Date of Birth", required=True, help="Date of Birth")
    #professor_choose = fields.Many2one('professor.professor', string='Professor')
    tasks_name = fields.Many2one('task.task', string='Task names')
    tasks_done = fields.Boolean(related='tasks_name.task_done', string='is done')
    task_fro=fields.One2many('task.task','task_id',string='task fro')



    @api.constrains("phoneno")
    def check_mobile_no(self):
        if str(self.phoneno) != 'False':
            if not str(self.phoneno).isdigit():
                raise ValidationError("Please enter valid mobile no.")
            else:
                if len(str(self.phoneno).strip()) != 10:
                    raise ValidationError("mobile no. size must be 10.")
