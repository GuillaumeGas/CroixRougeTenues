# -*- coding: utf-8 -*-
from openerp import api, models, fields

class EtatVetement(models.Model):
	_name = 'croixrouge.etat_vetement'
	
	name = fields.Char(string="Name", required=True)