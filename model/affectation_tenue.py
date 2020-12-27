# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
import logging
_logger = logging.getLogger(__name__)
	
class AffectationTenue(models.Model):
	_name = 'croixrouge.affectation_tenue'
	
	benevole_id = fields.Many2one('croixrouge.benevole', string="Bénévole", required=True, ondelete='set null')
	vetement_ids = fields.Many2many('croixrouge.vetement', string="Vêtements")
	
	mission_id = fields.Many2one('croixrouge.mission', string="Mission", required=False, ondelete='set null')
	date_retour = fields.Date(string="Date de retour", required=True, default=fields.Date.today())
	est_en_retard = fields.Boolean(compute="_est_en_retard", default=False)
	
	@api.multi
	def _est_en_retard(self):
		for affectation in self:
			date_retour = fields.Date.from_string(affectation.date_retour)
			date_courante = fields.Date.from_string(fields.Date.today())
			if date_retour < date_courante:
				affectation.est_en_retard = True
			else:
				affectation.est_en_retard = False				
				
	@api.model
	def create(self, values):
		etat_affecte = 1
		
		for entry in values['vetement_ids']:
			(a, b, vetement_ids) = entry
			for vetement_id in vetement_ids:
				vetement = self.env['croixrouge.vetement'].search([('id', '=', vetement_id)])
				vetement[0].write({'etat': etat_affecte})
				
		res = super(AffectationTenue, self).create(values)
		return res
		
	@api.multi
	def unlink(self):
		for affectation in self:
			etat_disponible = 0
		
			for vetement in affectation.vetement_ids:
				vetement.write({'etat': etat_disponible})
			
			return super(AffectationTenue, self).unlink()