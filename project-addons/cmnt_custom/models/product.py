# -*- coding: utf-8 -*-
# © 2016 Comunitea - Javier Colmenero <javier@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from openerp import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    treatment_days = fields.Integer('Treatment Days')
    notify_days = fields.Integer('Notice Before End Treatment')


class ProductProduct(models.Model):
    _inherit = 'product.product'


    def _check_ean_key(self, cr, uid, ids, context=None):
        """
        No Check CHECK EAN13 to do importation easly
        """
        res = True
        return res

    _constraints = [(_check_ean_key, 'You provided an invalid "EAN13 Barcode" reference. You may use the "Internal Reference" field instead.', ['ean13'])]
