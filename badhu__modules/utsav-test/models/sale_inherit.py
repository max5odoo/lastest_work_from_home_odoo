# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleInherit(models.Model):
    _inherit = 'sale.order'

    commission1 = fields.Many2one('hr.employee', string="Commission 1")
    commission2 = fields.Many2one('hr.employee', string="Commission 2")
    commission_history_ids = fields.One2many('commission.history', 'sale_id', string="Commission History")

    def calculate_commission(self):
        # if not self.commission_history_ids:
        for rec in self:
            if rec.commission1:
                if not rec.commission2:
                    history_data = [
                                    (0, 0, {
                                        'name': rec.commission1.id,
                                        'commission_price': (rec.amount_total*2.5)/100
                                    })]
                    rec.write({
                        'commission_history_ids': history_data,
                    })
                if self.commission2:
                    history_data = [(0, 0, {
                                        'name': rec.commission1.id,
                                        'commission_price': (rec.amount_total*2.5)/100
                                    }),
                                    (0, 0, {
                                        'name': rec.commission2.id,
                                        'commission_price': (rec.amount_total * 2.5) / 100
                                    })
                                    ]
                    rec.write({
                        'commission_history_ids': history_data,
                    })

    @api.onchange('commission1', 'commission2')
    def onchange_commission(self):
        """ Updates the commission user"""
        if self.commission_history_ids:
            if self.commission1.id != self.commission_history_ids[0].name:
                self.commission_history_ids[0].write({
                    "name": self.commission1.id
                })
            if self.commission2.id != self.commission_history_ids[1].name:
                self.commission_history_ids[1].write({
                    "name": self.commission2.id
                })