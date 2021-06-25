{
    'name': "manthan",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'website', 'sale'],

    # always loaded
    'data': [
        'security/security_prac.xml',
        'security/ir.model.access.csv',

        # 'data/student_data.xml',
        'data/student_cron.xml',
        'reports/report_template_id.xml',
        'reports/report.xml',
        'views/student_detail_page.xml',
        'views/student_registration_page.xml',
        'views/homepage.xml',
        'views/user_registration.xml',
        'views/student_login_page.xml',
        # 'views/contact_website_task_inherit.xml',
        'views/email_sending_template.xml',
        'views/email_mail_sending_wizard.xml',
        'views/professor.xml',
        'views/task.xml',
        'views/students.xml',
        'views/product_catalog.xml',
        'views/sale_product_catalog.xml',
        'views/wizard_demo.xml',
        'views/website_snippet.xml',
        'views/simple_student_page_render.xml',

        'reports/inherit_sale_report.xml',
        'reports/purchase_task_report.xml',
        # 'reports/delivery_task_report.xml',
        # 'views/sale_customer_invoice_inherit.xml',
        'data/student_mail_template.xml',
        'views/website_task.xml',
        'views/wizard_mail_task.xml',
        # 'views/task_set_values_wizard.xml'
        # 'views/task_fruits.xml',
        # 'views/button_prac.xml',
        # 'views/sale_order_updates.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False
}
# -*- coding: utf-8 -*-
