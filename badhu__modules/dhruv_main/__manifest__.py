

# -*- coding: utf-8 -*-
{
    'name': "NewApp",

    'summary': """
        This is a NewApp """,

    'description': """
        Short description of module's purpose of NewApp
    """,

    'author': "NewApp Company",
    'website': "http://www.newcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'dhruv_main_2', 'course__portal', 'hr', 'mail', 'sale', 'account', 'calendar', 'portal', 'website', ],

    # always loaded
    'data': [
        'security/student_detail_security.xml',
        'security/ir.model.access.csv',
        'reports/report_config.xml',
        'wizard/student_fees_wizard_view.xml',
        'data/email_sending_template.xml',
        'data/stu_data.xml',
        'wizard/email_mail_sending_wizard.xml',
        'wizard/student_import_record_wizard_view.xml',
        'data/student_mail_template.xml',
        'wizard/student_mail_view.xml',
        'wizard/student_courses_wizard_view.xml',
        'wizard/student_activity_wizard_view.xml',
        'views/course_lines.xml',
        'views/student_detail.xml',
        'views/student_xapth_demo.xml',
        'views/professor_detail.xml',
        'views/employee_document_detail.xml',
        'views/res_config_settings_view.xml',
        'reports/student_info_report.xml',
        'reports/sale_report_update.xml',
        # 'reports/delivery_slip_report.xml',
        'views/updated_xml.xml',
        'data/test_email.xml',
        'data/student_cron.xml',
        'views/frontend/hello_world_view.xml',
        'views/frontend/student_registration_form.xml',
        'views/frontend/homepage.xml',
        'views/frontend/students.xml',
        'views/frontend/student_login.xml',
        'views/frontend/student_profile.xml',
        'views/frontend/my_account_update.xml',
        'views/frontend/student_list.xml',
        'views/frontend/student_portal_template.xml',
        'views/frontend/course_portal_template.xml',
        'views/frontend/student_add_portal.xml',
        'views/custom_new_snippet.xml',
        'views/update_website_builder.xml',
        'views/frontend/student_table.xml',




    ],
    # only loaded in demonstration mode
    'demo': [
    ],

    'installable': True,
    'application': True,
    'auto_install': False
}
