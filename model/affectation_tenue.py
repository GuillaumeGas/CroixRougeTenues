# -*- coding: utf-8 -*-
from openerp import api, models, fields

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