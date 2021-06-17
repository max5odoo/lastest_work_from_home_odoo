from odoo import models


class ProductNameGet(models.Model):
    _inherit = "product.product"

    def name_get(self):
        res = super(ProductNameGet, self).name_get()
        data = []
        if self.env.context.get('ms'):
            for product in self:
                display_value = f"{product.name}######[{product.default_code}]"
                data.append((product.id, display_value))
            return data
        return res