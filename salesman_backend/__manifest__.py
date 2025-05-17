{
    'name': 'إدارة المناديب الميدانيين',
    'version': '1.0.0',
    'summary': 'نظام متابعة المناديب وخطط الزيارات الأسبوعية',
    'description': """
        نظام متكامل لإدارة:
        - ملفات المناديب
        - خطط الزيارات الأسبوعية
        - المسارات المحددة
        - سجل الزيارات
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'category': 'Sales',
    'depends': ['base', 'contacts', 'account'],
    'data': [
        'security/ir_rule.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/salesman_views.xml',
        'views/weekly_route_views.xml',
        'views/route_views.xml',
        'views/visit_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
