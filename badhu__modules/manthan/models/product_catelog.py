from odoo import fields, models


class Product_Catelog(models.Model):
    _name = 'product.catalog'
    _description = 'this is product catelog'

    name = fields.Char()
    description = fields.Char()
    product_catelog_ids = fields.One2many('product.catalog.lines', 'product_id')
