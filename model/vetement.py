# -*- coding: utf-8 -*-
from openerp import api, models, fields

class Vetement(models.Model):
	_name = 'croixrouge.vetement'
	
	type_id = fields.Many2one('croixrouge.type_vetement', string="Type", required=True, ondelete='set null')
	etat_id = fields.Many2one('croixrouge.etat_vetement', string="State", required=True, ondelete='set null')
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
	
	code_couleur = fields.Integer(compute='_get_code_couleur')
	
	@api.multi
	def _get_code_couleur(self):
		for vet in self:
			if vet.etat_id.name == "Disponible":
				vet.code_couleur = 0
			elif vet.etat_id.name == "Affecté":
				vet.code_couleur = 1
			else:
				vet.code_couleur = 2