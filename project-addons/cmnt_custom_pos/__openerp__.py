# -*- coding: utf-8 -*-
# © 2016 Comunitea - Javier Colmenero <javier@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'CMNT Custom POS',
    'version': '8.0.0.0.0',
    'author': 'Comunitea ',
    "category": "Stock",
    'license': 'AGPL-3',
    'depends': [
        'base',
        'point_of_sale',
        'crm'
    ],
    'contributors': [
        "Comunitea ",
        "Javier Colmenero <javier@comunitea.com>"
    ],
    "data": [
        'views/templates.xml',
    ],
    "demo": [
    ],
    'test': [
    ],
    'qweb': [
        'static/src/xml/view_meetings.xml',
    ],
    "installable": True
}
