# -*- coding: utf-8 -*-
# © 2016 Comunitea - Javier Colmenero <javier@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from openerp import models, fields, api
from datetime import datetime, timedelta


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    notify_date = fields.Datetime('Notify Date')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_ship_create(self):
        """
        Update date to notify customer from a customiced action
        """
        res = super(SaleOrder, self).action_ship_create()
        for order in self:
            for line in order.order_line:
                prod = line.product_id
                if prod.treatment_days and prod.notify_days:
                    current_date = datetime.now()
                    days = prod.treatment_days - prod.notify_days
                    notify_date = current_date + timedelta(days)
                    notify_date_str = datetime.strftime(notify_date,
                                                        '%Y-%m-%d %H:%M:%S')
                    line.notify_date = notify_date_str
        return res
