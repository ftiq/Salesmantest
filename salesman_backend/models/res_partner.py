from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    salesman_id = fields.Many2one(
        'salesman.profile',
        string='المندوب المسؤول',
        ondelete='set null'  # إضافة هذه السطر مهمة
    )
