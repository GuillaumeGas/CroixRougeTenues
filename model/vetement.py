# -*- coding: utf-8 -*-
from openerp import api, models, fields

class Vetement(models.Model):
	_name = 'croixrouge.vetement'
	
	type_id = fields.Many2one('croixrouge.type_vetement', string="Type", required=True, ondelete='set null')
	etat = fields.Selection([
		(0, 'Disponible'),
		(1, 'Affecté'),
		(2, 'Lavage'),
		], string="Etat", default=0)
	taille = fields.Selection([
		('XS', 'XS (36)'),
		('S', 'S (38)'),
		('M', 'M (40)'),
		('L', 'L (42)'),
		('XL', 'XL (44)'),
		('XXL', 'XXL (46)'),
		('XXXL', 'XXXL (48)'),
		], string="Taille", default='M')
	unite_locale_id = fields.Many2one('croixrouge.unite_locale', string="UL", required=True, ondelete='set null')