#-*- coding: utf-8 -*-

from odoo import models, fields, api


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