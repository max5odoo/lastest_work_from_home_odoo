# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class school_practice(models.Model):
#     _name = 'school_practice.school_practice'
#     _description = 'school_practice.school_practice'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
