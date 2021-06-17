from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class Teamleader(models.Model):
    _name = 'teamleader.teamleader'
    _description = 'Team leader description'
    _inherit = ['website.published.mixin', 'mail.thread', 'mail.activity.mixin']
    _rec_name = 'team_leader_name'

    team_leader_profile = fields.Image('Profile Picture', max_width=300, max_height=500)
    team_leader_id = fields.Char('Team Id')
    team_leader_name = fields.Char('Name', required=True)
    team_leader_address = fields.Text('Address')
    team_leader_phoneno = fields.Char('Contact No')
    team_leader_email_id = fields.Char('Email Id')
    dob = fields.Date(string="Date of Birth", required=True, help="Date of Birth")
    male = fields.Boolean()
    female = fields.Boolean()
    team_leader_short_desc = fields.Text('Enter Your Short Description')
    company_name = fields.Char("Company Name")
    trainee_team_leader=fields.Many2one('trainee.trainee',string='your trainee')
    team_leader_country = fields.Many2one('res.country', 'Country')

    @api.constrains("team_leader_phoneno")
    def check_mobile_no(self):
        if str(self.team_leader_phoneno) != 'False':
            if not str(self.team_leader_phoneno).isdigit():
                raise ValidationError("Please enter valid mobile no.")
            else:
                if len(str(self.team_leader_phoneno).strip()) != 10:
                    raise ValidationError("mobile no. size must be 10.")
