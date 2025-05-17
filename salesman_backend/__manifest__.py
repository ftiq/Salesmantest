{
    'name': 'Salesman Backend',
    'version': '1.0',
    'summary': 'إدارة المناديب والمسارات',
    'description': 'نظام متكامل لإدارة فرق المبيعات الميدانية',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'category': 'Sales',
    'depends': ['base', 'sale', 'account', 'contacts', 'stock'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'data': [
        # 🛡️ ملفات الصلاحيات أولاً
        'security/ir.model.access.csv',

    

    ],
}
