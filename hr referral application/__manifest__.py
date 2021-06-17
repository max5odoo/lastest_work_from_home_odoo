# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'refer',
    'version': '14.0.1.0.0',
    'summary': 'hr referral details',
    'sequence': 10,
    'description': """Here is a HR module for referral application""",
    'category': '',
    'website': '',
    'depends': ['base','contacts', 'hr', 'hr_recruitment', 'website'],
    'data': [
        'security/ir_rule_security_view.xml',
        'security/ir.model.access.csv',
        'data/website_menu.xml',
        'views/hr_referral_application_view.xml',
        'views/website_view_template.xml',
        'views/referral_submit_template_view.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

