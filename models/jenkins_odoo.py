# -*- coding: utf-8 -*-

from odoo import api, models, _

import jenkins


class IrCronMethods(models.TransientModel):
    _name = 'ir.cron.methods'

    @api.model
    def _jenkins_build_job(self, job):
        params = self.env['ir.config_parameter']
        jenkins_url = params.sudo().get_param('jenkins_ci.url', default='')
        jenkins_user = params.sudo().get_param('jenkins_ci.user', default='')
        jenkins_password = params.sudo().get_param('jenkins_ci.password', default='')
        server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_password)
        server.build_job(job)