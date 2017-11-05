# -*- coding: utf-8 -*-
{
    'name': 'Odoo Jenkins',
    'version': '10.0',
    'author': 'Odoo Community',
    'summary': 'Odoo Jenkins Plugin',
    'description': """
# Odoo Jenkins Plugin

Odoo Jenkins Plugin allows:
* start a Jenkins Job based on a Scheduled Action
* check jobs status without leaving Odoo UI

# Requirements

* Python Jenkins - http://python-jenkins.readthedocs.io/en/latest/index.html

pip install -r requirements.txt
    """,
    'category': 'Authentication',
    'depends': [
        'base'
    ],
    'data': [
        'views/templates.xml',
        'views/jenkins_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'qweb': [
        "static/src/xml/jenkins_dashboard.xml",
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
