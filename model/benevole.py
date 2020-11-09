# -*- coding: utf-8 -*-
from openerp import api, models, fields

class Benevole(models.Model):
	_name = 'croixrouge.benevole'
	
	name = fields.Char(string="Name", required=True)
	