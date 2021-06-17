# -*- coding: utf-8 -*-



{
    'name': "Wizard Report in Sale",

    'summary': """
        Wizard Report in Sale""",

    'description': """
        Wizard Report in Sale
    """,

    'author': "Shivam Kachhia",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'report',
    'version': '14.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['sale_management'],

    # always loaded
    'data': [
        'report/report.xml',
        'wizard/sale_report_wizard.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'application': True,
    'auto_install': False,
}






