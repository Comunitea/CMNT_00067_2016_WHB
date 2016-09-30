# -*- coding: utf-8 -*-
# © 2016 Comunitea - Javier Colmenero <javier@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, fields


class ResPartner(models.Model):

    _inherit = 'res.partner'

    diabetes_mellitus = fields.Boolean('Diabetes Mellitus')
    arterial_hypertension = fields.Boolean('Arterial Hypertension')
    dyslipidemia = fields.Boolean('Dyslipidemia')
    saos = fields.Boolean('SAOS')
    osteoarthritis = fields.Boolean('Osteoarthritis')
    depresion = fields.Boolean('Depresion')
    anxiety = fields.Boolean('Anxiety')
    eating_behavior_disorder = fields.Boolean('Eating Behavior Disorder')
    sop = fields.Boolean('SOP')
    thyroid_disease = fields.Boolean('Thyroid Disease')
    hepatic_steatosis = fields.Boolean('Hepatic Stealosis')
    toxic_habits = fields.Boolean('Toxic Habits')
    current_medication = fields.Char('Current Medication')

    family_obesity = fields.Boolean('Family Obesity')
    family_diabetes_mellitus = fields.Boolean('Diabetes Mellitus')
    family_arterial_hypertension = fields.Boolean('Arterial Hypertension')
    familty_dyslipidemia = fields.Boolean('Dyslipidemia')
    family_sleep_apnea = fields.Boolean('Sleep Apnea')
    family_thyroid_disease = fields.Boolean('Thyroid Disease')

    birth_weight = fields.Float('Birth weight')
    weight_20 = fields.Float('20 years weight')
    max_weight = fields.Float('Max weight')
    age_weight = fields.Integer('Age gain weight')
    cause_weight = fields.Char('Subjective cause gain weight')
    regime_done = fields.Boolean('Done previoous regime')
    consume_slim_down = fields.Boolean('Consume Slim products')
    weight_up_down = fields.Char('Weight up and down')
    eat_anxiety = fields.Char('Exists eat anxiety')
    eat_picking = fields.Boolean('Exists Picking')
    hide_eating = fields.Boolean('Hide eating')
    big_eating = fields.Boolean('Big eating')
    intestinal_rhythm = fields.Char('Intestinal Rhytm')
    num_pregnancies = fields.Integer('Num pregnancies')
    sons_birth_weight = fields.Float('Sons Birth weight')
    gain_weight = fields.Float('Gain weight pregnancies')
    gestacional_diabetes = fields.Boolean('Gestacional Diabetes')
    menopause = fields.Boolean('Menopause')

    food_query = fields.Text('Remainder 24h')

    blood_pressure = fields.Float('Blood Presure')
    weight = fields.Float('Weight')
    size = fields.Float('Size')
    bmi = fields.Float('Body mass index')
    basal_energy = fields.Float('Basal energy expenditure')
    contour_waist = fields.Float('Contour waist')
    boimpe = fields.Boolean('Boimpedanciometric')
