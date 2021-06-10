# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class orm(models.Model):
    _name = 'orm.methods'
    _description = 'ORM Methods'

    name = fields.Char(string="Name")
    dob = fields.Date(string='Date of Birth')
    age = fields.Integer(compute="age_count", string='Age', store=True)
    about = fields.Text(string='About')
    now = fields.Date()



    @api.depends('dob')
    def age_count(self):
        today = date.today()
        for rec in self:
            if rec.dob:
                rec.age = abs((today-rec.dob).days//365)

    @api.model
    def create(self, vals):
        vals['now'] = date.today()
        print(f"\n\n\n----------now-----{vals}-\n\n\n")
        res = super(orm, self).create(vals)
        return res

    def write(self, vals):
        print(f"\n\n\n----------vals-----{vals}-\n\n\n")

        res = super(orm, self).write(vals)
        return res
