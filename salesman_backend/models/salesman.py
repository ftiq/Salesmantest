from odoo import models, fields

class SalesmanProfile(models.Model):
    _name = 'salesman.profile'
    _description = 'بطاقة المندوب'

    name = fields.Char(string='اسم المندوب', required=True)
    mobile = fields.Char(string='موبايل')
    branch = fields.Many2one('res.branch', string='الفرع')
    
    # تغيير العلاقة إلى Many2many كحل بديل
    customer_ids = fields.Many2many(
        'res.partner',
        string='العملاء',
        relation='salesman_partner_rel',  # اسم جدول الربط
        column1='salesman_id',
        column2='partner_id'
    )
    
    payment_ids = fields.One2many('account.payment', 'salesman_id', string='قسائم الدفع')
