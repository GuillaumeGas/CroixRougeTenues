# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
import logging
_logger = logging.getLogger(__name__)
	
class AffectationTenue(models.Model):
	_name = 'croixrouge.affectation_tenue'
	
	benevole_id = fields.Many2one('croixrouge.benevole', string="Bénévole", required=True, ondelete='set null')
	type_tenue_id = fields.Many2one('croixrouge.type_tenue', string="Type de tenue", required=True, ondelete='set null')
	
	mission_id = fields.Many2one('croixrouge.mission_id', string="Mission", required=False, ondelete='set null')
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
		etat_disponible = 0
		etat_affecte = 1
		
		type_tenue = self.env['croixrouge.type_tenue'].search([('id', '=', values['type_tenue_id'])])
		for type_vetement_id in type_tenue.type_vetement_ids:
			vetement_dispo = self.env['croixrouge.vetement'].search(['&', ('type_id', '=', type_vetement_id.id), ('etat', '=', etat_disponible)])
			if (len(vetement_dispo) == 0):
				vetement = self.env['croixrouge.type_vetement'].search([('id', '=', type_vetement_id.id)])
				raise exceptions.ValidationError("Pas assez de " + vetement.name + " en stock")
				
		for type_vetement_id in type_tenue.type_vetement_ids:
			vetement_dispo = self.env['croixrouge.vetement'].search(['&', ('type_id', '=', type_vetement_id.id), ('etat', '=', etat_disponible)])
			vetement_dispo[0].write({'etat': etat_affecte})
				
		res = super(AffectationTenue, self).create(values)
		return res
		
	@api.multi
	def unlink(self):
		for affectation in self:
			etat_disponible = 0
			etat_affecte = 1
		
			type_tenue = self.env['croixrouge.type_tenue'].search([('id', '=', affectation.type_tenue_id.id)])	
			for type_vetement_id in type_tenue.type_vetement_ids:
				vetement_affecte = self.env['croixrouge.vetement'].search(['&', ('type_id', '=', type_vetement_id.id), ('etat', '=', etat_affecte)])
				if len(vetement_affecte) > 0:
					vetement_affecte[0].write({'etat': etat_disponible})
			
			return super(AffectationTenue, self).unlink()