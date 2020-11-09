# -*- coding: utf-8 -*-
from openerp import api, models, fields

class TypeVetement(models.Model):
	_name = 'croixrouge.type_vetement'
	
	name = fields.Char(string="Name", required=True)