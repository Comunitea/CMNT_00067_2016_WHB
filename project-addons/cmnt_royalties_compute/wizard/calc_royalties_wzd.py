# -*- coding: utf-8 -*-
# © 2016 Comunitea - Javier Colmenero <javier@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from openerp import models, fields, api, _
import calendar
from datetime import datetime


MONTHS = [
    ('1', _('January')), ('2', _('February')), ('3', _('March')), ('4', _('April')),
    ('5', _('May')), ('6', _('June')), ('7', _('July')), ('8', _('August')),
    ('9', _('September')), ('10', _('October')), ('11', _('November')),
    ('12', _('December')),
]


class CalcRoyaltiesWzd(models.TransientModel):

    _name = 'calc.royalties.wzd'

    @api.model
    def _get_dafault_month(self):
        res = '1'
        month = datetime.now().month
        if month == 1:
            month = 12
        else:
            month -= 1
        res = str(month)
        return res

    month = fields.Selection(MONTHS, 'Select Month', required=True,
                             default=_get_dafault_month)

    @api.multi
    def calc_royalties(self):
        self.ensure_one()
        print "Calculo royalty"
        year = datetime.now().year
        month = int(self.month)
        last_day = calendar.monthrange(year, month)[1]
        year = str(year)
        last_day = str(last_day)
        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)

        start_date = '-'.join([year, month, '01'])
        end_date = '-'.join([year, month, last_day])
        print start_date
        print end_date
        domain = [
            ('calc_royalties', '=', True),
            ('state', '=', 'open'),
            ('company_id', '=', 1)
        ]
        for c in self.env['account.analytic.account'].search(domain):
            self._cr.execute("""
                select sum(amount_untaxed)
                from sale_order
                where state in ('progress', 'manual', 'done') and
                partner_id = %s and company_id=1 and
                (date_order>='%s') and (date_order<='%s')
                """ % (c.partner_id.id, start_date + ' 00:00:00',
                       end_date + ' 00:00:00'))
            total = self._cr.fetchall()[0][0]
            if total is not None:
                royalty_amount = total * (c.royalty_per / 100.0)
                print total
                print royalty_amount
                self.env['royalty'].create({
                    'name': '/',
                    'amount': royalty_amount,
                    'contract_id': c.id,
                    'month': self.month,
                })


