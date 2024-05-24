# -*- coding: utf-8 -*-
{
    'name': "Electronic guide",

    'summary': """
        Electronic shipping guide
""",

    'description': """
        Electronic shipping guide
    """,

    'author': "Odoo",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Warehouse',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'stock',
        'fleet',
        'account',
        #'stock_picking_batch',
        'product_expiry',
        'l10n_pe_cpe',
        'l10n_pe_stock',
        'sistemerp_ereport_template',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/pe_sunat_eguide_view.xml',
        'views/company_view.xml',
        'views/stock_view.xml',
        'views/report_invoice.xml',
        'views/res_partner_view.xml',
        'data/sunat_eguide_data.xml',
        'report/report_picking.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
