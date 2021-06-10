# -*- coding: utf-8 -*-

{
    'name': "School",

    'summary': """
        Relational Fields""",

    'description': """
        Relational Fields : One2many, many2one, many2many
    """,

    'author': "Shivam Kachhia",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'School',
    'version': '14.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['sale_management',
                'mail','website',
                'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/partner_data.xml',
        'data/user_data.xml',
        # 'security/rec_rules.xml',
        'views/menus.xml',
        'wizard/regi_wizard_view.xml',
        'views/student_view.xml',
        'views/manthan.xml',
        'views/shivam.xml',
        'views/course_view.xml',
        'views/batch_view.xml',
        'views/registration_view.xml',
        'views/professor_view.xml',
        'report/report.xml',
        # 'report/personal_layout.xml',
        'report/student_report.xml',
        'report/registration_report.xml',
        # 'report/batch_report.xml',
        'report/sale_report_inherite.xml',
        # 'report/sale_total_all.xml',
        # 'views/column_invisible.xml',
        # 'data/studentdata.xml',
        # 'data/cron.xml',
        # 'data/coursedata.xml',
        # 'data/batchdata.xml',
        'data/mail_template.xml',
        # 'views/student_skills.xml',
        'views/website_template.xml',
        'views/student_webpage.xml',
        'views/registration_form_webpage.xml',
        'views/my_account_student.xml',
        # 'views/student_report_onclick.xml',
        'views/product_name_get.xml',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'application': True,
    'auto_install': False,
}






