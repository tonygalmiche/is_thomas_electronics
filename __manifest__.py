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
        #"account_voucher",
        #"account_accountant",
        "sale_management",
        "purchase",
        "stock",
        "mrp",
        "l10n_fr",
        #"sale_order_dates",       # Ajout de champs dates dans les commandes clients (date demandée)
    ],
    "init_xml" : [],
    "demo_xml" : [],
    "data" : [
        "views/product_view.xml",
        # "views/report_mrpbomstructure.xml",
        # "views/report_mrporder.xml",
        # "views/report_purchaseorder.xml",
        "views/partner_view.xml",
        "views/sale_view.xml",
        "views/purchase_view.xml",
        "views/is_suivi_commande.xml",
        "report/report_invoice.xml",
        "report/report_templates.xml",
        "report/report_deliveryslip.xml",
        "security/ir.model.access.csv",
    ], 
    "installable": True,
    "active": False, 
    "application": True,
    "license": "LGPL-3",
}

