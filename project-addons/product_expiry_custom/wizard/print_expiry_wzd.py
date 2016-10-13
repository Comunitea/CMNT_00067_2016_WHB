# -*- coding: utf-8 -*-
# © 2016 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, fields, api, _
import datetime


class PrintExpiryWzd(models.TransientModel):
    _name = 'print.expiry.wzd'

    days = fields.Integer('Days')
    company_id = fields.Many2one('res.company',
                                 default=lambda self:
                                 self.env['res.company'].
                                 _company_default_get('account.invoice'),)

    @api.multi
    def view_expiry(self):
        self.ensure_one()
        days = self.days
        current_date = fields.datetime.now()
        search_date = current_date + datetime.timedelta(days=days)
        date = search_date.strftime('%Y-%m-%d 00:00:00')
        today_date = current_date.strftime('%Y-%m-%d 00:00:00')
        res = {
            'domain': "[('life_date', '<=', '" + date + "'), ('life_date', '>', '" + today_date + "'), '|', ('company_id', '=', False), ('company_id', '=', '" + str(self.company_id) + "')]",
            'name': _('Print Expiry'),
            'view_type': 'form',
            'view_mode': 'tree,graph',
            'res_model': 'product.expiry.alert',
            'type': 'ir.actions.act_window',
            # 'context': ctx,
        }
        return res
