# -*- coding: utf-8 -*-
# © 2016 Comunitea - Javier Colmenero <javier@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from openerp import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    x_warehouse_ids = \
        fields.Many2many('res.users',
                         'x_stock_warehouse_res_users_x_warehouse_ids_rel',
                         'id2', 'id1', string='Allowed warehouses')