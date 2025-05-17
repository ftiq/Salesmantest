from odoo import models, fields

class DailyRouteLine(models.Model):
    _name = 'salesman.daily.route.line'
    _description = 'تفاصيل خط السير اليومي'

    daily_route_id = fields.Many2one(
        'salesman.daily.route',
        string='خط السير',
        required=True,
        ondelete='cascade'
    )
    customer_id = fields.Many2one(
        'res.partner',
        string='العميل',
        required=True
    )
    sequence = fields.Integer(string='الترتيب')
    visited = fields.Boolean(string='تمت الزيارة', default=False)
