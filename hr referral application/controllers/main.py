# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request, Controller
from odoo.addons.website_form.controllers.main import WebsiteForm


class SaleOrders(Controller):

    @http.route(['/form/hr_referral'], type='http', auth="public", website=True)
    def referral_form(self, **post):

        return request.render("hr referral application.hr_referral_form_template", {})
   
    @http.route('/referral/form/submit', type='http', auth='public', website=True)
    def hr_referral_details(self, **post):
        referral = request.env['hr.referral.application'].create({
                'name': post.get('name'),
                'email': post.get('email'),
                'referral_name': post.get('referral_name'),
                'degree': post.get('degree'),
                'department': post.get('department'),
                'expected_salary': post.get('expected_salary'),
                'expected_joing_date': post.get('expected_joing_date'),
                'summary': post.get('summary')
        })
        
        vals = {
                'referral': referral,
        } 
        return request.render("hr referral application.tmp_referral_form_success", vals)