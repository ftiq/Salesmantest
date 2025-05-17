{
    'name': 'Salesman Backend',
    'version': '1.0.0',
    'summary': 'إدارة المناديب والدفعات مع ربط المستودع والعملاء',
    'description': "تطبيق لإدارة بطاقات المناديب مع ارتباط بالمستودع والعملاء والدفعات.",
    'author': 'Business Technology',
    'website': 'https://www.yourcompany.com',
    'category': 'Sales',
    'depends': ['base', 'contacts', 'account', 'stock'],
    'data': [
        'views/salesman_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}