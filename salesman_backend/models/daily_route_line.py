from odoo import models, fields

class WeeklyRouteDay(models.Model):
    _name = 'salesman.weekly.route.day'
    _description = 'يوم في خط السير الأسبوعي'

    weekly_route_id = fields.Many2one(
        'salesman.weekly.route',
        string='خط السير الأسبوعي',
        required=True,
        ondelete='cascade'
    )
    day_of_week = fields.Selection([
        ('0', 'السبت'),
        ('1', 'الأحد'),
        ('2', 'الإثنين'),
        ('3', 'الثلاثاء'),
        ('4', 'الأربعاء'),
        ('5', 'الخميس'),
        ('6', 'الجمعة')
    ], string='يوم الأسبوع', required=True, default='0')
    route_id = fields.Many2one(
        'salesman.route',
        string='المسار',
        required=True
    )
