# -*- coding: utf-8 -*-
{
    'name': 'Odoo Jenkins',
    'version': '10.0',
    'author': 'Odoo Community',
    'summary': 'Odoo Jenkins CI Plugin',
    'description': """
# Odoo Jenkins Plugin

Odoo Jenkins-CI Plugin allows:
* start a Jenkins Job based on a Scheduled Action
* check jobs status without leaving Odoo UI

# Requirements

* Python Jenkins - http://python-jenkins.readthedocs.io/en/latest/index.html

pip install -r requirements.txt

Then go to:

Settings >> Technical >> Parameters >> System Parameters

Add/set the following params:
* jenkins_ci.url
* jenkins_ci.user
* jenkins_ci.password

Settings >> Technical >> Automation >> Jenkins Dashboard
    """,
    'category': 'Authentication',
    'depends': [
        'base', 'web'
    ],
    'data': [
        'views/templates.xml',
        'views/jenkins_views.xml',
        'data/ir_cron.xml'
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
