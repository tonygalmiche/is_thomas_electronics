# -*- coding: utf-8 -*-

from odoo import fields, models


class res_partner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    is_contact           = fields.Char("Contact principal")
    is_code_tiers_client = fields.Char("Code tiers client")
