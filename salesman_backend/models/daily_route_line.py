from odoo import models, fields, api

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
    
    location_lines = fields.One2many(
        'salesman.weekly.route.location',
        'day_id',
        string='المواقع المخطط زيارتها'
    )

class WeeklyRouteLocation(models.Model):
    _name = 'salesman.weekly.route.location'
    _description = 'موقع في خط السير اليومي'

    day_id = fields.Many2one(
        'salesman.weekly.route.day',
        string='اليوم',
        required=True,
        ondelete='cascade'
    )
    location_type = fields.Selection([
        ('area', 'منطقة حسب العنوان'),
        ('route', 'مسار محدد مسبقاً')
    ], string='نوع الموقع', default='area', required=True)
    
    # حقول المنطقة (عند اختيار نوع 'area')
    area_type = fields.Selection([
        ('city', 'المدينة'),
        ('zip', 'الرمز البريدي'),
        ('street', 'الحي/الشارع')
    ], string='نوع المنطقة')
    
    area_value = fields.Char(string='قيمة المنطقة')
    
    # حقول المسار (عند اختيار نوع 'route')
    predefined_route_id = fields.Many2one(
        'salesman.route',
        string='مسار محدد'
    )
    
    sequence = fields.Integer(string='ترتيب الزيارة', default=1)
    notes = fields.Text(string='ملاحظات')
    customer_ids = fields.Many2many(
        'res.partner',
        string='العملاء في هذا الموقع',
        compute='_compute_customer_ids',
        store=True
    )

    @api.depends('location_type', 'area_type', 'area_value', 'predefined_route_id')
    def _compute_customer_ids(self):
        for rec in self:
            if rec.location_type == 'area' and rec.area_type and rec.area_value:
                domain = []
                if rec.area_type == 'city':
                    domain = [('city', '=', rec.area_value)]
                elif rec.area_type == 'zip':
                    domain = [('zip', '=', rec.area_value)]
                elif rec.area_type == 'street':
                    domain = ['|', ('street', 'ilike', rec.area_value), 
                             ('street2', 'ilike', rec.area_value)]
                
                rec.customer_ids = self.env['res.partner'].search(domain)
            
            elif rec.location_type == 'route' and rec.predefined_route_id:
                rec.customer_ids = rec.predefined_route_id.customer_ids

    @api.onchange('location_type')
    def _onchange_location_type(self):
        if self.location_type == 'route':
            self.area_type = False
            self.area_value = False
        else:
            self.predefined_route_id = False