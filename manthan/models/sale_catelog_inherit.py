from odoo import fields, models


class Sale_Catelog_Inherit(models.Model):
    _inherit = 'sale.order'
    product_catelog_id = fields.Many2one('product.category')
