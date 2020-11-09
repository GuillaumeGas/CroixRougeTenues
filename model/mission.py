# -*- coding: utf-8 -*-
from openerp import api, models, fields

class Mission(models.Model):
	_name = 'croixrouge.mission'
	
	nom = fields.Char(string="Nom", required=True)
	date = fields.Date(string="Date", required=True, default=fields.Date.today())
	
	unite_locale_id = fields.Many2one('croixrouge.unite_locale', string="Unité locale", required=True, ondelete='set null')
	responsable_id = fields.Many2one('croixrouge.responsable', string="Responsable", required=True, ondelete='set null')
	
	affectation_tenue_ids = fields.One2many('croixrouge.affectation_tenue', 'mission_id', string="Affectations tenue")