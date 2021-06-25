from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class Trainee(models.Model):
    _name = 'trainee.trainee'
    _description = 'Trainee Description'
    _inherit = ['website.published.mixin', 'mail.thread', 'mail.activity.mixin']
    _rec_name = 'trainee_name'

    trainee_profile = fields.Binary()
    trainee_id = fields.Char('Trainee Id', required=True)
    trainee_name = fields.Char('Name', required=True)
    trainee_address = fields.Text('Address')
    trainee_phoneno = fields.Char('Contact No', required=True)
    trainee_email_id = fields.Char('Email Id', required=True)
    dob = fields.Date(string="Date of Birth", required=True, help="Date of Birth")
    male = fields.Boolean()
    female = fields.Boolean()
    trainee_short_desc = fields.Text('Enter Your Short Description')
    company_name = fields.Char("Company Name")
    trainee_country = fields.Many2one('res.country', 'Country')


    @api.constrains("trainee_phoneno")
    def check_mobile_no(self):
        if not self.trainee_phoneno.isdigit():
            raise ValidationError("Please enter valid mobile no.")
        else:
            if len(self.trainee_phoneno) != 10:
                raise ValidationError("mobile no. size must be 10.")
