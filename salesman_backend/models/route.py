from odoo import models, fields

class SalesmanRoute(models.Model):
    _name = 'salesman.route'
    _description = 'مسار المندوب'

    name = fields.Char(string='اسم المسار', required=True)
    salesman_id = fields.Many2one('salesman.profile', string='المندوب')
    customer_ids = fields.Many2many('res.partner', string='العملاء')
