# -*- coding: utf-8 -*-
# © 2016 Comunitea - Javier Colmenero <javier@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from openerp import models, fields

MONTHS = [
    ('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'),
    ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'),
    ('9', 'September'), ('10', 'October'), ('11', 'November'),
    ('12', 'December'),
]


class Royalty(models.Model):
    _name = "royalty"

    contract_id = fields.Many2one('account.analytic.account', 'Contract')
    name = fields.Char('Name')
    amount = fields.Float('Amount', readonly=True)
    month = fields.Selection(MONTHS, 'Select Month', required=True)
