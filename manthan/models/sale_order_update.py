from odoo import models, fields, api


class Sale_Order_Up(models.Model):
    _inherit = "sale.order"

    is_ready = fields.Boolean()
    is_dt = fields.Boolean()

    product_catalogs_id = fields.Many2one('product.catalog')

    @api.onchange("product_catalogs_id")
    def product_cat_id(self):
        for rec in self:
            many2one_field = rec.product_catalogs_id.id
            print(f'\n\n\n\n\n{many2one_field}\n\n\n\n')
            rec.env['product.catalog.lines'].search([]).write({
                'is_active': False
            })
            product_find = rec.env['product.catalog.lines'].search([('product_id', '=', many2one_field)]).write({
                'is_active' : True
            })
            print(f'\n\n\n\n\nthis is product find--->{product_find}\n\n\n\n')



class Sale_Order_Lines_Product(models.Model):
    _inherit = "sale.order.line"

    product_catelog_product_line_id = fields.Many2one('product.catalog.lines')
    description = fields.Char(related='product_catelog_product_line_id.description')
