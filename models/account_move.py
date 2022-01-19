# -*- coding: utf-8 -*-
from odoo import fields, models, api

class account_move(models.Model):
    _inherit = "account.move"

    @api.depends('invoice_line_ids')
    def _compute_is_partner_liv_id(self):
        partner_id = self.partner_id.id
        if self.partner_shipping_id:
            partner_id=self.partner_shipping_id.id

        self.is_partner_liv_id = partner_id


    is_partner_liv_id = fields.Many2one('res.partner', string='Adresse de livraison', compute='_compute_is_partner_liv_id')



