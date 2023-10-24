# -*- coding: utf-8 -*-
{
    'name': "Zaltek Customizations",

    'summary': """
        Hide Manage Databases links on login page""",

    'description': """
        General customizations
    """,

    'author': "Zaltek Digital",
    'website': "https://zaltek.co.uk",

    # Categories can datbe used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        'views/login_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
