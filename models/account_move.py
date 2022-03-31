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


    @api.depends('invoice_line_ids')
    def _compute_is_sale_id(self):
        for obj in self:
            sale_id = False
            for invoice_line in obj.invoice_line_ids:
                for line in invoice_line.sale_line_ids:
                    sale_id=line.order_id.id
            obj.is_sale_id = sale_id


    is_partner_liv_id   = fields.Many2one('res.partner', string='Adresse de livraison', compute='_compute_is_partner_liv_id')
    is_sale_id          = fields.Many2one('sale.order', string='Commande client', compute='_compute_is_sale_id')
    #is_client_order_ref = fields.Char(string='Référence commande client', compute='_compute_is_client_order_ref')



