from odoo import http
from odoo.http import request

class XtraAPIController(http.Controller):

    def _authenticate_token(self):
        token = request.httprequest.headers.get('Authorization')
        if not token or not token.startswith('Bearer '):
            return None

        token = token[7:]  # Strip "Bearer "
        user = request.env['res.users'].sudo().search([('api_token', '=', token)], limit=1)
        if not user:
            return None

        request.uid = user.id  # Impersonate user
        return user

    def _auth_required(self):
        user = self._authenticate_token()
        if not user:
            return {'error': 'Unauthorized'}, 401
        return None  # authorized

    @http.route('/api/contacts', type='json', auth='public', methods=['GET'], csrf=False)
    def get_contacts(self):
        auth = self._auth_required()
        if auth:
            return auth

        contacts = request.env['res.partner'].sudo().search([('customer_rank', '>', 0)])
        return [
            {
                'id': c.id,
                'name': c.name,
                'email': c.email,
                'phone': c.phone,
                'mobile': c.mobile,
                'salesman_id': c.user_id.name if c.user_id else None,
            }
            for c in contacts
        ]

    @http.route('/api/salesmen', type='json', auth='public', methods=['GET'], csrf=False)
    def get_salesmen(self):
        auth = self._auth_required()
        if auth:
            return auth

        salesmen = request.env['salesman.profile'].sudo().search([])
        return [
            {
                'id': s.id,
                'name': s.name,
                'mobile': s.mobile,
                'warehouse': s.warehouse_id.name if s.warehouse_id else None,
                'customers': [p.name for p in s.customer_ids],
            }
            for s in salesmen
        ]

    @http.route('/api/visits', type='json', auth='public', methods=['GET'], csrf=False)
    def get_visits(self):
        auth = self._auth_required()
        if auth:
            return auth

        visits = request.env['salesman.visit.log'].sudo().search([])
        return [
            {
                'id': v.id,
                'salesman': v.salesman_id.name if v.salesman_id else None,
                'customer': v.customer_id.name if v.customer_id else None,
                'date': v.date.strftime('%Y-%m-%d %H:%M:%S'),
                'status': v.status,
                'notes': v.notes,
            }
            for v in visits
        ]

    @http.route('/api/products', type='json', auth='public', methods=['GET'], csrf=False)
    def get_products(self):
        auth = self._auth_required()
        if auth:
            return auth

        products = request.env['product.product'].sudo().search([])
        return [
            {
                'id': p.id,
                'name': p.display_name,
                'default_code': p.default_code,
                'qty_available': p.qty_available,
                'free_qty': p.qty_available - p.outgoing_qty,
                'uom': p.uom_id.name,
            }
            for p in products
        ]
