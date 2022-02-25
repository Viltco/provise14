from odoo import api, fields, models, _


class KRA(models.Model):
    _name = "kra.info"
    _description = "KRA"
    _rec_name = 'name'


    name = fields.Char(string='KRA Name')
    kra_weight = fields.Integer(string='KRA Weight %')
    hr_weight = fields.Integer(string='HR Weight %')
    kra_number = fields.Char(string='KRA Number', required=True, copy=False, readonly=True, default='New')
    Text = fields.Text(string='Description', tracking=True)

    @api.model
    def create(self, values):
        values['kra_number'] = self.env['ir.sequence'].next_by_code('kra.info') or _('New')
        return super(KRA, self).create(values)





