# -*- coding: utf-8 -*-
from openerp import models, api, fields
class res_partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    dni = fields.Char(string="DNI")
    _sql_constraints = [
        ('dni', 'unique(dni)', 'The DNI must be unique')
        ]