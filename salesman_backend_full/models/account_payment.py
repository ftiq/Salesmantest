from odoo import models, fields

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    salesman_id = fields.Many2one('salesman.profile', string='المندوب')