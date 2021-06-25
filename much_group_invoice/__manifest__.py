# -*- coding: utf-8 -*-

{
    "name": "much. | Group Invoice",
    "summary": """An Odoo Module creates a group invoice for multiple invoices.""",
    "description": """""",
    "author": "much. GmbH",
    "website": "https://muchconsulting.de",
    # for the full list
    "category": "Accounting/Accounting",
    "version": "14.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": [
        "account",
    ],
    # always loaded
    "data": [
        # "security/ir.model.access.csv",
        "reports/report_config.xml",
        "reports/group_invoices_template.xml",
        "views/invoice_button.xml",
        "views/account_invoice_inherit.xml",
    ],
}
