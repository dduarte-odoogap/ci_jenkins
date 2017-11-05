# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import json


class JenkinsController(http.Controller):

    @http.route('/web/jenkins/jobs', type='json', auth='user')
    def jenkins_get_jobs(self, **kw):
        params = request.env['ir.config_parameter']
        jenkins_url = params.sudo().get_param('jenkins_url', default='')

        # import jenkins
        # server = jenkins.Jenkins('http://10.167.140.228:8080/', username='dduarte', password='admin')
        # jobs = server.get_jobs()
        # server.get_job_info('Test')

        res = [
            {"id": 1, "name": 'Job 1'},
            {"id": 2, "name": 'Job 2'},
        ]
        return {
            'jobs': res
        }