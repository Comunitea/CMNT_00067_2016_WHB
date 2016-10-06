# -*- coding: utf-8 -*-

from openerp import models, api, fields
from openerp.osv import osv, fields as fields2

class res_partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    
    dni = fields.Char(string="DNI")
    
    _sql_constraints = [
        ('dni', 'unique(dni)', 'The DNI must be unique')
        ]

# Clase para extender modelo producto con descripcion corta

class product_template(models.Model):
	_inherit = 'product.template'
   
	short_summary = fields.Char(string="Short Summary")

# Clase para extender modelo categoria de producto con descripcion

class product_public_category(osv.osv):
	_inherit = "product.public.category"
	    
	short_description = fields.Char(string="Short Description")