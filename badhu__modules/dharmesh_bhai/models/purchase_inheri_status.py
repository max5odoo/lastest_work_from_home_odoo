from odoo import fields, models


class purchase_inheri_status(models.Model):
    _inherit = "purchase.order"

    state = fields.Selection(selection_add=[('process', 'Process')])
