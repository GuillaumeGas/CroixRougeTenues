# -*- coding: utf-8 -*-
from openerp import api, models, fields

class UniteLocale(models.Model):
	_name = 'croixrouge.unite_locale'
	
	name = fields.Char(string="Name", required=True)
	