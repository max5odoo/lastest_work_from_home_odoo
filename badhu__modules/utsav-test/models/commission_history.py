from odoo import api, fields, models


class CommissionHistory(models.Model):

    _name = 'commission.history'
    _description = 'commission.history'

    name = fields.Many2one('hr.employee', string="Name")
    sale_id = fields.Many2one('sale.order', string="Sale order")
    commission_percentage = fields.Float(string="Commission Percentage", default=2.5, store=True)
    commission_price = fields.Float(string="Commission Price", compute="_compute_price", store=True)

    @api.depends('commission_percentage', 'sale_id.amount_total')
    def _compute_price(self):
        for rec in self:
            rec.commission_price = (rec.sale_id.amount_total*rec.commission_percentage) / 100