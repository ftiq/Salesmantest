from odoo import models, fields

class SalesmanProfile(models.Model):
    _name = 'salesman.profile'
    _description = 'بطاقة المندوب'

    # الحقول الأساسية
    name = fields.Char(string='اسم المندوب', required=True)
    mobile = fields.Char(string='موبايل')

    # المستودع
    warehouse_id = fields.Many2one('stock.warehouse', string='المستودع')

    # العملاء المرتبطين
    customer_ids = fields.Many2many(
        'res.partner',
        string='العملاء',
        relation='salesman_partner_rel',
        column1='salesman_id',
        column2='partner_id'
    )

    # قسائم الدفع المرتبطة
    payment_ids = fields.One2many('account.payment', 'salesman_id', string='قسائم الدفع')

    # 🔐 صلاحيات متفرقة - جميعها Boolean
    allow_add_new_customer = fields.Boolean(string='السماح بإضافة زبائن جديدة')
    return_needs_approval = fields.Boolean(string='الإرتجاع الجديد يتطلب موافقة الإدارة')
    photo_required_for_new_customer = fields.Boolean(string='صورة الزبون الجديد مطلوبة')
    allow_update_customer_data = fields.Boolean(string='السماح بتحديث معلومات الزبون')
    allow_zone_update = fields.Boolean(string='السماح بتحديث موقع الزبون')
    enforce_route_commitment = fields.Boolean(string='الإلتزام بالمسار فقط لزيارات المندوب')
    allow_off_route_visits = fields.Boolean(string='السماح بزيارات خارج المسار')
    force_visit_location = fields.Boolean(string='الموقع إجباري')
    enforce_visit_closure_location = fields.Boolean(string='الالتزام بالموقع عند إغلاق الزيارة')
    visit_notes_required = fields.Boolean(string='ملاحظات الزيارة مطلوبة عند إلغاء الزيارة')
    enforce_visit_time = fields.Boolean(string='تفعيل الحد الزمني لأوقات الزيارة')
    restrict_clients_to_route = fields.Boolean(string='تفعيل عملاء المسار فقط ضمن المسار')
    check_exit_from_route = fields.Boolean(string='التحقق من المسار عند عملية الخروج')
    check_exit_time = fields.Boolean(string='مراقبة بصمة الخروج عند الخروج')

    # إعدادات فواتير/أسعار/خصومات
    verify_debt_ceiling = fields.Boolean(string='التحقق من سقف الدين للزبون')
    verify_credit_days = fields.Boolean(string='التحقق من عدد الذمة للزبون')
    allow_return_invoice = fields.Boolean(string='الفواتير الإحالة ممنوعة للزبون')
    return_invoice_limit = fields.Boolean(string='التحقق من عدد فواتير الإحالة المستحقة')
    debt_ceiling_per_salesman = fields.Boolean(string='التحقق من سقف الدين للمندوب')
    allow_misc_discounts = fields.Boolean(string='السماح بخصم المشروبات')
    allow_discount_by_percentage = fields.Boolean(string='السماح بتعديل نسبة خصم')
    apply_discount_on_receipt = fields.Boolean(string='نمط السند')
    allow_discount_on_items = fields.Boolean(string='السماح بتعديل نسبة خصم المواد')
    allow_edit_prices = fields.Boolean(string='السماح بتعديل الأسعار')
    allow_edit_invoice = fields.Boolean(string='السماح بتعديل الفاتورة')
    bind_prices_to_category = fields.Boolean(string='ربط الأسعار مع تصنيفات تلقائيًا')
    show_materials_without_stock = fields.Boolean(string='إظهار المواد التي بلا رصيد')
    hide_stock_in_invoice = fields.Boolean(string='عدم إظهار رصيد المواد في الفواتير')
    allow_liquid_sales = fields.Boolean(string='السماح بعمليات المواد السائلة')
    allow_invoice_sales = fields.Boolean(string='السماح بالمبيعات السائلة')

    # Report Permissions
    report_allow_statement = fields.Boolean(string="منع استعراض كشف صندوق المندوب")
    report_allow_aging = fields.Boolean(string="منع استعراض أعمار الذمم")
    report_allow_invoices = fields.Boolean(string="منع استعراض فواتير المندوب")
    report_allow_visits = fields.Boolean(string="منع استعراض زيارات المندوب")
    report_allow_offers = fields.Boolean(string="منع استعراض تقرير العروض")
    report_allow_account = fields.Boolean(string="منع استعراض كشف الحساب")
    report_allow_debts = fields.Boolean(string="منع استعراض مديونية المندوب")
    
    # Duration fields
    duration_1 = fields.Char(string="المدة المسموحة ١")
    duration_2 = fields.Char(string="المدة المسموحة ٢")
    duration_3 = fields.Char(string="المدة المسموحة ٣")
    # Daily Page Fields Permissions
    daily_block_sales_total = fields.Boolean(string="منع استعراض اجمالي المبيعات")
    daily_block_orders_total = fields.Boolean(string="منع استعراض اجمالي الطلبات")
    daily_block_returns_total = fields.Boolean(string="منع استعراض اجمالي المرتجع")
    daily_block_requests_total = fields.Boolean(string="منع استعراض اجمالي طلبات المرتجع")
    daily_block_previous_balance = fields.Boolean(string="منع استعراض الرصيد السابق")
    daily_block_expenses = fields.Boolean(string="منع استعراض المشروبات")
    daily_block_payments = fields.Boolean(string="منع استعراض المدفوعات")
    
    daily_block_current_balance = fields.Boolean(string="منع استعراض الرصيد الحالي")
    daily_block_daily_visits = fields.Boolean(string="منع استعراض الزيارات اليومية")
    daily_block_pending_visits = fields.Boolean(string="منع استعراض الزيارات المتأخرة")
    daily_block_skipped_visits = fields.Boolean(string="منع استعراض الزيارات المتخطية")
    sale_order_ids = fields.One2many('sale.order', 'salesman_id', string="طلبات البيع")
    daily_block_promotional_sales = fields.Boolean(string="منع استعراض المبيعات الترويجية")
    daily_block_total_sales = fields.Boolean(string="منع استعراض المبيعات")
    
    daily_block_return_invoices = fields.Boolean(string="منع استعراض الفواتير الاحالة المستحقة")
    daily_block_approved_return_invoices = fields.Boolean(string="منع استعراض الفواتير الاحالة المسموحة")
