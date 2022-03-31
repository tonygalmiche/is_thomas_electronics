# -*- coding: utf-8 -*-
{
    "name" : "InfoSaône - Module Odoo 15 pour Thomas Electronics",
    "version" : "0.1",
    "author" : "InfoSaône / Tony Galmiche",
    "category" : "InfoSaône",
    "description": """
InfoSaône - Module Odoo 15 pour Thomas Electronics
===================================================

InfoSaône - Module Odoo 15 pour Thomas Electronics
""",
    "maintainer": "InfoSaône",
    "website": "http://www.infosaone.com",
    "depends" : [
        "base",
        "mail",
        "calendar",
        "crm",
        "sale_management",
        "purchase",
        "purchase_stock",
        "stock",
        "mrp",
        "l10n_fr",
    ],
    "init_xml" : [],
    "demo_xml" : [],
    "data" : [
        "views/account_move_view.xml",
        "views/mrp_view.xml",
        "views/product_view.xml",
        "views/partner_view.xml",
        "views/sale_view.xml",
        "views/purchase_view.xml",
        "views/is_suivi_commande.xml",
        "report/report_invoice.xml",
        "report/report_mrporder.xml",
        "report/report_templates.xml",
        "report/report_deliveryslip.xml",
        "report/report_purchaseorder.xml",
        "security/ir.model.access.csv",
    ], 
    "installable": True,
    "active": False, 
    "application": True,
    "license": "LGPL-3",
}

