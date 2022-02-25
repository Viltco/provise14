from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class KPIData(models.Model):
    _name = "kpi.data"
    _description = "KPI Data"
    _rec_name = 'kpi_name'


    kpi_name = fields.Char(string='KPI Name')
    kpi_weight = fields.Integer(string='KPI Weight %')
    kpi_id = fields.Many2one('kpi.info', string='KPI INFO')





