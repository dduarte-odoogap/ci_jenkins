odoo.define('ci_jenkins.jenkins_dashboard', function (require) {
"use strict";

var core = require('web.core');
var Model = require('web.Model');
var Widget = require('web.Widget');
var Session = require('web.session');
var ajax = require('web.ajax');
var ControlPanelMixin = require('web.ControlPanelMixin');

var QWeb = core.qweb;
var _t = core._t;

var JenkinsDashboard = Widget.extend(ControlPanelMixin, {
    template: "jenkins.DashboardMain",

    events: {
        'click .o_run_jenkins_job': 'on_run_jenkins_job',
    },

    init: function(parent, context) {
        this._super(parent, context);

        this.jobs = [];

        this.dashboards_templates = ['jenkins.dashboard_jobs'];

    },

    willStart: function() {
        var self = this;
        return this._super().then(function() {
            return $.when(
                self.fetch_data()
            );
        });
    },

    fetch_data: function() {
        var self = this;
        return ajax.jsonRpc('/web/jenkins/jobs', 'call', {

        }).done(function(result) {
            self.data = result;
            self.jobs = result.jobs;
        });
    },

    start: function() {
        var self = this;
        return this._super().then(function() {
            self.render_dashboards();
        });
    },

    render_dashboards: function() {
        var self = this;
        console.log(self);
         _.each(this.dashboards_templates, function(template) {
             self.$('.o_jenkins_dashboard').append(QWeb.render(template, {widget: self}));
         });
    },

    on_run_jenkins_job: function(ev) {
        ev.preventDefault();
        var self = this;
        var jobName = ev.target.id.split("_").pop();
        ajax.jsonRpc('/web/jenkins/build','call',{"job":jobName.toString()});
    },

});

core.action_registry.add('jenkins_dashboard_start', JenkinsDashboard);

return JenkinsDashboard;

});
