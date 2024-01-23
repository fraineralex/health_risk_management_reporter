# __manifest__.py
{
    'name': 'ARS Template Export',
    'version': '13.0.1',
    'category': 'Accounting',
    'summary': 'ARS Template Export Module',
    'description': "ARS Template Export Module",
    'depends': ['account'],
    'data': [
        # views
        'views/ars_report_view.xml',
        
        # security
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
