# ملف: models/stock_picking.py
from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    salesman_id = fields.Many2one('salesman.profile', string="المندوب")
