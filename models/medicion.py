# -*- encoding: utf-8 -*-
from openerp import models,fields

class Medicion(models.Model):
	_name='uniquindio.tiposensor'

	estacion_id = fields.Many2one(string='Estacion',required=True,comodel_name='uniquindio.estacion')
	tipo_id = fields.Many2one(string='Tipo',required=True,comodel_name='uniquindio.tiposensor')	
	valor = fields.Char('Valor', required=True)
	unidad = fields.Char('Unidad Medida', required=True)
