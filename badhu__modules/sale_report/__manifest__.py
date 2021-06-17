# -*- coding: utf-8 -*-


{
    'name': "Report Sale",

    'summary': """
        Report sale""",

    'description': """
       
    """,

    'author': "Shivam Kachhia",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sale',
    'version': '14.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['sale_management'],

    # always loaded
    'data': [
        'report/custom_total_for_selected.xml',
        # 'wizard/sale_wizard.xml',
        # 'wizard/wizard_menu.xml',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'application': True,
    'auto_install': False,
}







