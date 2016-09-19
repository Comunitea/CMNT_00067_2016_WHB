# -*- coding: utf-8 -*-
# © 2016 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, tools


class ProductExpiryAlert(models.Model):

    _name = 'product.expiry.alert'
    _auto = False

    name = fields.Many2one('stock.production.lot')
    alert_date = fields.Datetime()
    life_date = fields.Datetime()
    product = fields.Many2one('product.product')

    def init(self, cr):
        tools.drop_view_if_exists(cr, self._table)
        cr.execute("""CREATE VIEW product_expiry_alert AS (
SELECT id, id as name, life_date, alert_date, product_id as product
FROM stock_production_lot WHERE alert_date < now())""")
