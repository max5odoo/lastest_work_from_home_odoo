from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    api_key = fields.Char()

    #    minlength = fields.Integer("Minimum Password Length", help="Minimum number of characters passwords must contain, set to 0 to disable.")

    # @api.model
    # def get_values(self):
    #     res = super(ResConfigSettings, self).get_values()

    #     res['minlength'] = int(self.env['ir.config_parameter'].sudo().get_param('auth_password_policy.minlength', default=0))

    #     return res

    # @api.model
    # def set_values(self):
    #     self.env['ir.config_parameter'].sudo().set_param('auth_password_policy.minlength', self.minlength)

    #     super(ResConfigSettings, self).set_values()

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()

        res['api_key'] = self.env['ir.config_parameter'].sudo(
        ).get_param('dhruv_main.api_key')

        print(f"\n\n\n{res['api_key']}\n\n\n")

        return res

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].set_param(
            "dhruv_main.api_key", self.api_key)  #
        super(ResConfigSettings, self).set_values()




class MailResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    mail_template_id = fields.Many2one('mail.template')

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].set_param(
            "mail_template_id", self.mail_template_id.id)  #
        res = super(ResConfigSettings, self).set_values()

    # @api.model
    # def get_values(self):
    #     res = super(ResConfigSettings, self).get_values()

    #     res['mail_template_id'] = self.env['ir.config_parameter'].sudo(
    #     ).get_param('mail_template_id')

    #     return res
