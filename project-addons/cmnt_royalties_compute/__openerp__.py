# -*- coding: utf-8 -*-
# © 2016 Comunitea - Javier Colmenero <javier@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'CMNT Royalties compute',
    'version': '8.0.0.0.0',
    'author': 'Comunitea ',
    "category": "Stock",
    'license': 'AGPL-3',
    'depends': [
        'base',
        'analytic',
        'account_analytic_analysis'
    ],
    'contributors': [
        "Comunitea ",
        "Javier Colmenero <javier@comunitea.com>"
    ],
    "data": [
        'views/analytic_view.xml',
        'wizard/calc_royalties_wzd_view.xml'
    ],
    "demo": [
    ],
    'test': [
    ],
    "installable": True
}
