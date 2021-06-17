# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HrReferralApplication(models.Model):
    _name= 'hr.referral.application'
    _description = "Hr Referral Application"

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string= "Email")
    referral_name = fields.Many2one('hr.employee', string= "Referral Name", required=True)
    degree = fields.Many2one('hr.recruitment.degree', string= "Degree", required=True)
    department = fields.Many2one('hr.job', string = "Department", required=True)
    expected_salary = fields.Integer(string = "Expected Salary", required=True)
    summary = fields.Text(string = "Summary")
    expected_joing_date = fields.Date(string = "Expected Joing Date")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('cancel', 'Cancel')
    ], string='Status', readonly=True, required=True, tracking=True, copy=False, default='draft')

    def button_approve(self):
        self.write({'state': 'approved'})
        return {}

    def button_confirm(self):
        self.write({'state': 'approved'})
        return {}

    def button_cancel(self):
        self.write({'state': 'cancel'})
        return {}

    def button_draft(self):
        self.write({'state': 'draft'})
        return {}