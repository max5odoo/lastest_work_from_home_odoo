# -*- coding: utf-8 -*-


{
    'name': "student_app",

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
    'depends': ['sale_management', 'hr', 'mail', 'account', 'purchase'],

    # always loaded
    'data': [
        # "security/student_group_Access.xml",
        # "security/ir.model.access.csv",

        # 'reports/delevery_report_inherit.xml',

        'reports/report_button.xml',
        'reports/report_student.xml',

        # "security/ir.model.employee.csv",

        # 'views/views.xml',
        # 'views/templates.xml',
        # "views/model_upgrade.xml", not for res partner
        # "views/sale_order_update_view.xml",
        # 'views/ir_config_view_inherits.xml',
        'data/mail_templete.xml',
        'data/wizard_mail_templete.xml',
        "wizards/student_wizard_view.xml",
        "wizards/stu_mail_wizard_view.xml",

        'data/course_data_file.xml',
        'data/skill_data_file.xml',
        'data/student_data_file.xml',
        'data/student_data_lines_file.xml',

        'data/ir_cron_data.xml',

        "views/student_data_lines.xml",
        "views/student_corner.xml",
        "views/Configure_course.xml",
        "views/but_addon_action btn.xml",
        "views/Configure_skills.xml",
        "views/purchase_inheri_status.xml",
        # "views/hr_employee_update.xml",
        # "views/employee_document.xml",
        # "views/mango_task.xml",

        # "views/profile_web.xml",
        # "views/home_web.xml",
        # "views/signup_web.xml",
        # "views/login_web.xml",
        "views/website/homepage.xml",
        "views/website/inherit_account.xml",
        "views/website/portal_students.xml",
        "views/website/portal_student_view.xml",
        "views/website/portal_stu_course_view.xml",
        "views/website/portal_stu_course_view.xml",
        "views/website/portal_signup.xml",
        # "views/website/custom_snnipet.xml",

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',

    ],
    'installable': True,
    'auto_install': False,
    'application': True,  # for visual in admin as app install
}
