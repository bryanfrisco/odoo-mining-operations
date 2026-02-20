{
    'name': 'Mining Operations Management',
    'version': '17.0.1.0.0',
    'summary': 'Manage mining sites, heavy equipment, and daily production',
    'description': """
        Module for managing mining operations including:
        - Mining Site Management
        - Heavy Equipment Tracking
        - Daily Production Recording
        - Production Reports
    """,
    'author': 'Your Name',
    'category': 'Industries',
    'depends': ['base', 'mail', 'hr', 'maintenance'],
    'data': [
        'security/ir.model.access.csv',
        'views/mining_site_views.xml',
        'views/heavy_equipment_views.xml',
        'views/daily_production_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}