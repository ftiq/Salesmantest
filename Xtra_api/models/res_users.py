from odoo import models, fields, api
import secrets

class ResUsers(models.Model):
    _inherit = 'res.users'

    api_token = fields.Char(string="API Token", readonly=True)

    @api.model
    def create(self, vals):
        if not vals.get('api_token'):
            vals['api_token'] = secrets.token_urlsafe(32)
        return super().create(vals)
