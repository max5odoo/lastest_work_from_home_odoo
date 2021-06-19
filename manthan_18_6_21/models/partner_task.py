from odoo import api, fields, models


class Partner_task(models.Model):
    _inherit = 'res.partner'

    def name_get(self):
        partner_name_gets = []
        for rec in self:
            name = f"{rec.name}({rec.city})"
            partner_name_gets.append((rec.id, name))
        return partner_name_gets

    def _name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []
        domain = []
        if name:
            domain = [('city', operator, name)]
        return self._search(domain + args, limit=limit)
