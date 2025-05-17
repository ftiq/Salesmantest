from odoo import api, models, fields

class WeeklyRoute(models.Model):
    _name = 'salesman.weekly.route'
    _description = 'خط السير الأسبوعي للمندوب'

    name = fields.Char(string='الاسم', compute='_compute_name')
    date_from = fields.Date(string='من تاريخ', required=True)
    date_to = fields.Date(string='إلى تاريخ', required=True)
    salesman_id = fields.Many2one('salesman.profile', string='المندوب', required=True)
    day_lines = fields.One2many(
        'salesman.weekly.route.day',
        'weekly_route_id',
        string='أيام الأسبوع'
    )

    @api.depends('date_from', 'date_to', 'salesman_id')
    def _compute_name(self):
        for rec in self:
            rec.name = f"خط سير {rec.salesman_id.name or ''} من {rec.date_from} إلى {rec.date_to}"

    @api.constrains('date_from', 'date_to')
    def _check_dates(self):
        for rec in self:
            if rec.date_from > rec.date_to:
                raise models.ValidationError('تاريخ البداية يجب أن يكون قبل تاريخ النهاية')
