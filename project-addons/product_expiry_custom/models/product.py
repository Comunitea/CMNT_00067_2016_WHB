# -*- coding: utf-8 -*-
# © 2016 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, fields, api
from datetime import datetime


class ProductProduct(models.Model):

    _inherit = 'product.product'
    available_without_alert = fields.Float(compute='_get_non_alert_stock')

    @api.multi
    def action_view_alerts(self):
        action_xml_id = 'product_expiry_custom.action_product_expiry_alert'
        action = self.env.ref(action_xml_id).read()[0]
        action['domain'] = "[('product','in',[" + \
            ','.join(map(str, self.ids)) + "])]"
        return action

    @api.multi
    def _get_non_alert_stock(self):
        for product in self:
            domain_quant = [
                ('product_id', '=', product.id),
                ('lot_id.alert_date', '<',
                 datetime.now().strftime('%Y-%m-%d %H:%M:%S'))] + \
                product._get_domain_locations()[0]
            quants = self.env['stock.quant'].search(domain_quant)
            product.available_without_alert = product.qty_available - \
                sum(quants.mapped('qty'))
