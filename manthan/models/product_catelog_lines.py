from odoo import  fields, models


class Product_Catelog_Lines(models.Model):
    _name = 'product.catalog.lines'
    _description = 'this is product catelog lines'

    product_id=fields.Many2one('product.product')
    product_catelog_id=fields.Many2one('product.catalog')

