from odoo import models, fields

class VisitLog(models.Model):
    _name = 'salesman.visit.log'
    _description = 'سجل الزيارات'

    salesman_id = fields.Many2one('salesman.profile', string='المندوب')
    customer_id = fields.Many2one('res.partner', string='العميل')
    date = fields.Datetime(string='تاريخ الزيارة', default=fields.Datetime.now)
    notes = fields.Text(string='ملاحظات')
    status = fields.Selection([
        ('planned', 'مخطط'),
        ('completed', 'مكتمل'),
        ('cancelled', 'ملغى')
    ], string='الحالة')
