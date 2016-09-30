# -*- coding: utf-8 -*-
# © 2016 Comunitea - Javier Colmenero <javier@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from openerp import models, fields


class ProductProduct(models.Model):
    _inherit = 'product.template'

    treatment_days = fields.Integer('Treatment Days')
    notify_days = fields.Integer('Notice Before End Treatment')
