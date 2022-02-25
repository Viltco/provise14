from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class KPIData(models.Model):
    _name = "kpi.lines"
    _description = "KPI Lines"


    kpi_lines_id = fields.Many2one('kpi.data', string='KPI Data')
    kpi_weight = fields.Integer(string='KPI Weight %')

    kpi_ids = fields.Many2one('kpi.info', string='KPI Data')

    @api.onchange('kpi_lines_id')
    def set_price(self):
        for rec in self:
            rec.kpi_weight = rec.kpi_lines_id.kpi_weight











