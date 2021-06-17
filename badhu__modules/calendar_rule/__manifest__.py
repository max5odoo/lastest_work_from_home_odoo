# -*- coding: utf-8 -*-
{
    'name': "calendar_by_shivam",

    'summary': """
        record_rule_for_calendar""",

    'description': """
    """,

    'author': "Shivam Kachhia",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'calendar',
    'version': '14.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['calendar'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/rec_rule.xml',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'application': True,
    'auto_install': False,
}









