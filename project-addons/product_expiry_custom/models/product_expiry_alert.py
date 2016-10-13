# -*- coding: utf-8 -*-
# © 2016 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, tools


class ProductExpiryAlert(models.Model):

    _name = 'product.expiry.alert'
    _auto = False

    name = fields.Many2one('stock.production.lot')
    life_date = fields.Datetime()
    product_id = fields.Many2one('product.product')
    company_id = fields.Many2one('res.company',)

    def init(self, cr):
        tools.drop_view_if_exists(cr, self._table)
        cr.execute(
            """CREATE VIEW product_expiry_alert AS (
            select spl.id, spl.id as name, spl.life_date, spl.product_id,
                   pt.company_id
            from stock_production_lot spl
            inner join product_product pp on spl.product_id = pp.id
            inner join product_template pt on pp.product_tmpl_id = pt.id)""")
