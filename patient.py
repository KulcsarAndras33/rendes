#-*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Record'
    _rec_name = 'patient_name'

    patient_name = fields.Char('Name', required=True)
    patient_age = fields.Integer('Age')
    notes = fields.Text('Notes')
    image = fields.Binary('Image')
    gender = fields.Selection([('male', 'Male'),('female', 'Female'),('other', 'Other')], default='male', string='Gender')
    patient_isurgent = fields.Boolean('Is urgent')
    patient_urgency = fields.Integer('Urgency', store=True, readonly=True, compute='_compute_urgency')

    @api.depends('patient_age', 'create_date', 'patient_isurgent')
    def _compute_urgency(self):
        for rule in self:
            rule.patient_urgency = 1
            urgency_byage = abs(30 - rule.patient_age)
            urgency_bytime = (datetime.now() - rule.create_date).days
            if (rule.patient_isurgent):
                urgency_byisurgent = 70
            else:
                urgency_byisurgent = 0
            rule.patient_urgency += urgency_byage + urgency_bytime + urgency_byisurgent