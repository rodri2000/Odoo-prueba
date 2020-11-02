# -*- coding: utf-8 -*-
{
    'name': "Reto Final",

    'summary': """Controlar los trabajos
        """,

    'description': """
        Este modulo va a seguir a los alumnos para controlar su trabajo de fin 
        de grado
    """,

    'author': "Ander",
    'website': "http://www.ander.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Work',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/taskMenuItem.xml',
        'views/user.xml',
        'views/partner.xml',
        'views/report.xml'
        #'security/user_access_rules.xml'
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
        'installable': True, 
        'application': True,
        'auto_install': False,
        'qweb': []
}