# sale_order.py
from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    salesman_id = fields.Many2one('salesman.profile', string='المندوب')
