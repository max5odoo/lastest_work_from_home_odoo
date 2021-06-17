from odoo import fields, models, api
from odoo.osv import expression


class ProductCatelogLines(models.Model):
    _name = 'product.catalog.lines'
    _description = 'this is product catelog lines'

    name = fields.Char()
    description = fields.Char()
    product_id = fields.Many2one('product.catalog')
    is_active = fields.Boolean()

    # @api.model
    # def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
    #     args = args or []
    #     domain = [('description', operator, name)]
    #     return self._search(expression.AND([domain, args]), limit=limit)
