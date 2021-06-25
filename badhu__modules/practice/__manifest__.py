# -*- coding: utf-8 -*-
{
    'name': "Company Management",

    'summary': """
        This module is basically for managing the company's employees.   
        """,

    'description': """
        This module is used to search different team leaders,trainess.Apart from this we can find the relationship between them. 
    """,

    'author': "Max Associates",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/team_leader.xml',
        'views/trainee.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
