-*- coding: utf-8 -*-

from odoo import models, fields, api


class user(models.Model):
    _name = 'rendes.user'
    _description = 'rendes.user'

    name = fields.Char('Name')
    year = fields.Integer('Year')
