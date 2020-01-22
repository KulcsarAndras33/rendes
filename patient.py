#-*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta


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
    patient_doctor_name = fields.Many2one('hospital.doctor', string='Doctors name')


    @api.depends('patient_age', 'create_date', 'patient_isurgent')
    def _compute_urgency(self):
        for rule in self:
            rule.patient_urgency = 1
            urgency_byage = abs(30 - rule.patient_age)
            if (rule.patient_isurgent):
                urgency_byisurgent = 70
            else:
                urgency_byisurgent = 0
            rule.patient_urgency += urgency_byage + urgency_byisurgent


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Doctor Record'
    _rec_name = 'doctor_name'

    doctor_name = fields.Char('Name', required=True)
    doctor_age = fields.Integer('Age')
    notes = fields.Text('Notes')
    image = fields.Binary('Image')
    gender = fields.Selection([('male', 'Male'),('female', 'Female'),('other', 'Other')], default='male', string='Gender')
    doctor_professional_field = fields.Selection([('surgeon', 'Surgeon'), ('cardiologist', 'Cardiologist'), ('psychiatrist', 'Psychiatrist')], string='Professional Field')
    doctor_patients_name = fields.One2many('hospital.patient', 'patient_doctor_name')


class Appointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Appointment'
    _rec_name = 'doctor_name'

    doctor_name = fields.Many2one('hospital.doctor', string='Doctor')
    patient_name = fields.Char('Patient')
    start_date = fields.Datetime(string="Start")
    end_date = fields.Datetime(string="End Date", store=True, compute='_get_end_date', readonly=True)
    duration = fields.Integer(string="Minutes")

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue
            duration = timedelta(minutes=r.duration)
            r.end_date = r.start_date + duration

    @api.depends('doctor_name', 'patient_name')
    def _get_name(self):
        for r in self:
            r.label_name = r.doctor_name + ": " + r.patient_name