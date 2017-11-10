# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

import jenkins


class JenkinsController(http.Controller):

    def __init__(self):
        params = request.env['ir.config_parameter']
        self.jenkins_url = params.sudo().get_param('jenkins_ci.url', default='http://10.167.140.228:8080/')
        self.jenkins_user = params.sudo().get_param('jenkins_ci.user', default='dduarte')
        self.jenkins_password = params.sudo().get_param('jenkins_ci.password', default='admin')

    @http.route('/web/jenkins/jobs', type='json', auth='user')
    def jenkins_get_jobs(self, **kw):
        jenkins_url = self.jenkins_url
        jenkins_user = self.jenkins_user
        jenkins_password = self.jenkins_password
        server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_password)
        res = []
        jobs = server.get_jobs()
        for job in jobs:
            jid = {
                "color": job['color'],
                "name": job['name'],
                "healthReport": server.get_job_info(job['name'])['healthReport']
            }
            res.append(jid)

        return {
            'jobs': res
        }

    @http.route('/web/jenkins/build', type='json', auth='user')
    def jenkins_build_job(self, job, **kw):
        jenkins_url = self.jenkins_url
        jenkins_user = self.jenkins_user
        jenkins_password = self.jenkins_password
        server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_password)
        res = server.build_job(job)
        return {'result': res}

