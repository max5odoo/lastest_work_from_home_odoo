# -*- coding: utf-8 -*-
{
    'name': "manthan_18_6_21",

    'summary': """
       """,

    'description': """
       This is the module of sale order description.
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'sale_management', 'website', 'portal'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/sale_order_template.xml',
        'views/sale_order_data_submit.xml',
        'views/sale_order_inherit.xml',
        'views/final_sale_order_record.xml',
        'views/list_sale_order_show.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
