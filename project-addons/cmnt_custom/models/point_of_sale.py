# -*- coding: utf-8 -*-
# © 2016 Comunitea - Javier Colmenero <javier@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from openerp import models, fields, api
from datetime import datetime, timedelta


class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'

    notify_date = fields.Datetime('Notify Date')


class PosOrder(models.Model):
    _inherit = 'pos.order'

    @api.model
    def create_from_ui(self, order):
        order_ids = super(PosOrder, self).create_from_ui(order)
        for order in self.browse(order_ids):
            for line in order.lines:
                prod = line.product_id
                if prod.treatment_days and prod.notify_days:
                    current_date = datetime.now()
                    days = prod.treatment_days - prod.notify_days
                    notify_date = current_date + timedelta(days)
                    notify_date_str = datetime.strftime(notify_date, '%Y-%m-%d %H:%M:%S')
                    line.notify_date = notify_date_str
        return order_ids
