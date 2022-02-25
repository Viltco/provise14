from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import date, datetime


class KPIScore(models.Model):
    _name = "kpi.score"
    _description = "KPI Score"
    _rec_name = 'employee_id'


    employee_id = fields.Many2one('hr.employee', string='Employee Name')
    job_id = fields.Many2one('hr.job', string='Job Position')
    department_id = fields.Many2one('hr.department', string='Department')
    partner_id = fields.Many2one('res.partner', string='Line Manager')
    joining_date = fields.Date(string='Joining Date')
    review_Date = fields.Date(string='Review Date')
    period_review_from = fields.Date(string=' Period Review From')
    period_review_to = fields.Date(string='Period Review To')

    kpi_score_lines = fields.One2many('kpi.notebook', 'kpi_score_id')


    year = fields.Selection(
        selection='years_selection',
        string="Year",
        default="2021"
    )
    def years_selection(self):
        year = 2000
        year_list = []
        while year != 2030:
            year_list.append((str(year), str(year)))
            year += 1
        return year_list

    # @api.depends('kpi_score_lines.kpi_weight')
    # def _compute_weight_lines(self):
    #     for record in self:
    #         for line in record.add_notebook:

    def send_email(self):
        print("u click")
        for rec in self:
            template_id = rec.env.ref('kpi__kra.email_template').id
            template = rec.env['mail.template'].browse(template_id)
            template.send_mail(rec.id, force_send=True)







