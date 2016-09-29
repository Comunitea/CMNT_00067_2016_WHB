# -*- coding: utf-8 -*-
# © 2016 Comunitea - Javier Colmenero <javier@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models,fields


class ResPartner(models.Model):

    _inherit = 'res.partner'

    diabetes_mellitus = fields.Boolean('Diabetes Mellitus')
    arterial_hypertension = fields.Boolean('Arterial Hypertension')
    dyslipidemia = fields.Boolean('Dyslipidemia')
    saos = fields.Boolean('SAOS')
    osteoarthritis = fields.Boolean('Osteoarthritis')
    anxiety = fields.Boolean('Anxiety')
    eating_behavior_disorder = fields.Boolean('Eating Behavior Disorder')
    thyroid_disease = fields.Boolean('Thyroid Disease')
    hepatic_steatosis = fields.Boolean('Hepatic Stealosis')
    toxic_habits = fields.Boolean('Toxic Habits')
    current_medication = fields.Char('Current Medication')



