from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class KPI(models.Model):
    _name = "kpi.info"
    _description = "KPI"
    _rec_name = 'kra_id'


    kra_id = fields.Many2one('kra.info', string='KRA Name')
    kra_weight = fields.Integer(string='KRA Weight %', readonly="1")


    kpi_kra_id = fields.One2many('kpi.lines', 'kpi_ids' ,string='KPI DATA')
    total = fields.Integer(string='Total Petrol', compute="_compute_total_weight")




    @api.onchange('kra_id')
    def set_kra_weight(self):
        for rec in self:
            if rec.kra_id:
                rec.kra_weight = rec.kra_id.kra_weight

    @api.depends('kpi_kra_id.kpi_weight')
    def _compute_total_weight(self):
        weight = 0
        for record in self:
            for line in record.kpi_kra_id:
                weight += line.kpi_weight
            record.total = weight
            if record.total > record.kra_id.kra_weight:
                raise ValidationError(_("KPI Weight must have Less than or Equal to KRA Weight"))


    # def set_weight(self):
    #     for rec in self:
    #         if rec.total > rec.kra_id.kra_weight:
    #             raise ValidationError(_("KPI Weight must have Less than or Equal to KRA Weight"))
