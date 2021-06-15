from odoo import models, fields


class Sale_Order_Up(models.Model):
    _inherit = "sale.order"

    is_ready = fields.Boolean()
    is_dt = fields.Boolean()

    product_catalog_id = fields.Many2one('product.catalog')


class Sale_Order_Lines_Product(models.Model):
    _inherit = "sale.order.line"

    product_catelog_product_line_id = fields.Many2one('product.catalog.lines')
    description = fields.Char(related='product_catelog_product_line_id.description')
