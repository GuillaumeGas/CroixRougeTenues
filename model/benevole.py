# -*- coding: utf-8 -*-
from openerp import api, models, fields

class Benevole(models.Model):
	_name = 'croixrouge.benevole'
	
	nom = fields.Char(string="Nom", required=True)
	prenom = fields.Char(string="Prenom", required=True)
	nivol = fields.Char(string="Nivol", required=True)
	
	