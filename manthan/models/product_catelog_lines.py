from odoo import fields, models


class Product_Catelog_Lines(models.Model):
    _name = 'product.catalog.lines'
    _description = 'this is product catelog lines'

    name = fields.Char()
    description = fields.Char()
    product_id = fields.Many2one('product.catalog')
