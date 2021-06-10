from odoo import fields, api, models
from datetime import date


class UseAbstract(models.AbstractModel):
    _name = 'abstract.for.age'
    _description = 'Use of Abstract Model'

    dob = fields.Date(string="Date Of Birth")
    age = fields.Integer(string="Age", compute='compute_age', store=True, readonly=True)

    @api.depends('dob')
    def compute_age(self):
        today = date.today()
        for rec in self:
            if rec.dob:
                rec.age = abs((today - rec.dob).days // 365)