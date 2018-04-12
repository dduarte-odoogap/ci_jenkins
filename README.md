# Odoo Jenkins Plugin

Odoo Jenkins Plugin allows:
* start a Jenkins Job based on a Scheduled Action
* check jobs status without leaving Odoo UI

# Install and Setup

## Requirements

pip install python-jenkins

## Setup

Add this addons folder to odoo addons path, then install the module in
the respective Odoo server with matching version as this module. (10.0,
11.0)

In Settings >> Parameters >> System Parameters:

Set your Jenkins server parameters:

jenkins_ci.url (e.g. 'http://localhost:8080')
jenkins_ci.user (e.g. 'admin')
jenkins_ci.passwors (e.g. 'abcd')

## Cron Job

Create a Scheduled Job in Settings >> Automation >> Scheduled Jobs or
Using XML in your modules

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data noupdate="1">

        <!-- Example CI Job -->
        <record id="ir_cron_test_jenkins" model="ir.cron">
            <field name="name">Test jenkins job</field>
            <field name="jenkins_job" eval="True"/>
            <field name="active" eval="False"/>
            <field name="interval_type">minutes</field>
            <field name="interval_number">2</field>
            <field name="numbercall">-1</field>
            <field name="model">ir.cron.methods</field>
            <field name="function">_jenkins_build_job</field>
            <field eval="('Test')," name="args" />
        </record>

    </data>

</odoo>
```