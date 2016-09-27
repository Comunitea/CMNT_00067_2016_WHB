# -*- coding: utf-8 -*-
# © 2016 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Product expiry customizations",
    "summary": "",
    "description": """-remove use_date
    """,
    "version": "8.0.1.0.0",
    "category": "Product",
    "website": "comunitea.com",
    "author": "Comunitea",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
        "product_expiry"
    ],
    "data": [
        'views/stock_production_lot.xml',
        'views/product.xml',
        'views/product_expiry_alert.xml',
        'security/ir.model.access.csv'
    ],
}
