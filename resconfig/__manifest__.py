# -*- coding: utf-8 -*-
{
    'name': "RES COnfig",

    'summary': """
        RES""",

    'description': """
        Relational Fields : One2many, many2one, many2many
    """,

    'author': "Shivam Kachhia",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'RES',
    'version': '14.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [

        'views/res_config.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}









