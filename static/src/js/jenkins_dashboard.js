odoo.define('odoo_jenkins.jenkins_dashboard', function (require) {
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
        _.each(this.dashboards_templates, function(template) {
            self.$('.o_jenkins_dashboard').append(QWeb.render(template, {widget: self}));
        });
    },

});

core.action_registry.add('jenkins_dashboard_start', JenkinsDashboard);

return JenkinsDashboard;

});
