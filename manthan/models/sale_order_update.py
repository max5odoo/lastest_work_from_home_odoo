from odoo import models, fields


class Sale_Order_Up(models.Model):
    _inherit = "sale.order"

    is_ready = fields.Boolean()
    is_dt = fields.Boolean()
