from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    client_id = fields.Char(string='Client ID')
    api_key = fields.Char(string='API Key')
    customer = fields.Many2one('res.partener', string='customer')
    vandor = fields.Many2one('res.partener', string='vandor')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()

        res['client_id'] = self.env['ir.config_parameter'].sudo().get_param('client_id')
        res['api_key'] = self.env['ir.config_parameter'].sudo().get_param('api_key')
        res['customer'] = self.env['ir.config_parameter'].sudo().get_param('customer')
        res['vandor'] = self.env['ir.config_parameter'].sudo().get_param('vandor')

        print(f"\n\n--{res}--\n\n")

        return res

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].sudo().set_param(
            'client_id', self.client_id)
        self.env['ir.config_parameter'].sudo().set_param(
            'api_key', self.api_key)
        self.env['ir.config_parameter'].sudo().set_param(
            'customer', self.api_key)
        self.env['ir.config_parameter'].sudo().set_param(
            'vandor', self.api_key)

        super(ResConfigSettings, self).set_values()
