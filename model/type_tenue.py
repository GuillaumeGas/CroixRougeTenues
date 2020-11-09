# -*- coding: utf-8 -*-
from openerp import api, models, fields

class TypeTenue(models.Model):
	_name = 'croixrouge.type_tenue'
	
	name = fields.Char(string="Name", required=True)
	type_vetement_ids = fields.Many2many('croixrouge.type_vetement', string="Composition")
	