# -*- coding: utf-8 -*-
# © 2016 Comunitea - Javier Colmenero <javier@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from openerp import models, fields


class AccountAnalyticAccount(models.Model):
    _inherit = "account.analytic.account"

    calc_royalties = fields.Boolean('Subject to Royalties')
    royalty_per = fields.Float('Royalty Percentage')
    royalty_ids = fields.One2many('royalty', 'contract_id', 'Royalties')
