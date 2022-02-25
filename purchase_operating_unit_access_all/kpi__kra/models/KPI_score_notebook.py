from odoo import api, fields, models, _


class KPIScoreNotebook(models.Model):
    _name = "kpi.notebook"
    _description = "KPI Notebook"

    kpi_id = fields.Many2one('kpi.data', string='KPI')
    kra_id = fields.Many2one('kra.info', string='KRA')
    kpi_weight = fields.Integer(string='KPI Weight %', related ='kpi_id.kpi_weight')
    kra_weight = fields.Integer(string='KRA Weight %')
    target = fields.Integer(string='Target')
    achieve = fields.Integer(string='Achieve')
    achievements = fields.Integer(string='Achievements')
    score_a = fields.Integer(string='Score % A')
    score_b = fields.Integer(string='Score % B')

    kpi_score_id = fields.Many2one('kpi.score')



    @api.onchange('kra_id')
    def set_values(self):
        for record in self:
            rec = self.env['kpi.info'].search([('kra_id', '=', record.kra_id.id)])
            for i in rec:
                record.kra_weight = i.kra_id.kra_weight
                return {'domain': {'kpi_id' : [('id', '=', i.kpi_kra_id.kpi_lines_id.ids)]}}




    @api.onchange('target','achieve','achievements')
    def set_achievements(self):
        if self.target and self.achieve:
            self.achievements = ((self.achieve / self.target)*100)
            if self.achievements >= 100:
                self.score_a = self.kpi_weight
                self.score_b = self.kra_id.hr_weight
            else:
                self.score_a = ((self.achievements*self.kpi_weight)/ 100)
                self.score_b = ((self.achievements*self.kra_id.hr_weight)/ 100)











