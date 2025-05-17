# ملف: models/account_move.py
from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    salesman_id = fields.Many2one('salesman.profile', string="المندوب")
