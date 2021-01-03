# -*- coding: utf-8 -*-
from openerp import api, models, fields

class Responsable(models.Model):
	_name = 'croixrouge.responsable'
	
	name = fields.Char(string="Nom", required=True)
	prenom = fields.Char(string="Prenom", required=True)
	unite_locale_id = fields.Many2one('croixrouge.unite_locale', string="UL", required=True, ondelete='set null')
	