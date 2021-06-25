from odoo import models, fields, api


class ResConfigSettingsInherit(models.TransientModel):
    _inherit = 'res.config.settings'

    student_setting = fields.Char()

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].sudo().set_param(
            "student_setting", self.student_setting)
        res = super(ResConfigSettingsInherit, self).set_values()
        return res

    @api.model
    def get_values(self):
        res = super(ResConfigSettingsInherit, self).get_values()
        check = self.env['ir.config_parameter'].sudo(
        ).get_param("student_setting")
        print(f"\n\n\n\nhi su kare {check}\n\n\n\n")
        return res
