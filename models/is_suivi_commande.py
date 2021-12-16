# -*- coding: utf-8 -*-
from odoo import fields, models, tools

class is_suivi_commande(models.Model):
    _name="is.suivi.commande"
    _description = "Suivi commande"
    _order="commitment_month desc, partner_id, product_id"
    _auto = False


    partner_id           = fields.Many2one("res.partner", "Customer")
    product_id           = fields.Many2one("product.product", "Ref.")
    is_famille_id        = fields.Many2one("is.famille", "Family")
    is_emplacement_stock = fields.Char("Location")
    product_uom_qty      = fields.Float("Qty"                   , digits=(12,0))
    client_order_ref     = fields.Char("PO number")
    price_unit           = fields.Float("Unit price"            , digits=(12,0))
    currency_id          = fields.Many2one("res.currency", "Currency")
    #requested_date       = fields.Datetime("Shipment date requested")
    commitment_date      = fields.Datetime("Shipment date accepted")
    commitment_month     = fields.Char("Shipment month accepted")
    forecasted_turn_over = fields.Float("Forecasted Turn over"  , digits=(12,0))
    #shipped_qty          = fields.Float("Qty shipped"           , digits=(12,0))
    #real_shipment_date   = fields.Datetime("Real shipment date")
    #remaining_qty        = fields.Float("Remaining Qty"         , digits=(12,0))
    #turn_over_done       = fields.Float("Turn over done"        , digits=(12,0))
    so                   = fields.Char("SO")
    mo                   = fields.Char("MO")
    state                = fields.Char("État")

    def init(self):
        cr=self._cr
        tools.drop_view_if_exists(cr, "is_suivi_commande")


                # CREATE OR REPLACE FUNCTION is_shipped_qty(pp_id integer, so_id integer, OUT qty float) RETURNS float AS $$
                # BEGIN
                #     qty:=(
                #         select sum(sm.product_uom_qty) 
                #         from stock_picking sp inner join stock_move sm on  sp.id=sm.picking_id   
                #         where sp.document_id=so_id and sm.product_id=pp_id and sm.state="done"
                #     );

                #     IF qty is null THEN
                #         qty:=0;
                #     END IF;
                # END;
                # $$ LANGUAGE plpgsql;

                # CREATE OR REPLACE FUNCTION is_real_shipment_date(pp_id integer, so_id integer) RETURNS date AS $$
                # BEGIN
                #     RETURN (
                #         select max(sm.date) 
                #         from stock_picking sp inner join stock_move sm on  sp.id=sm.picking_id   
                #         where sp.document_id=so_id and sm.product_id=pp_id and sm.state="done"
                #     );
                # END;
                # $$ LANGUAGE plpgsql;



        cr.execute("""
                CREATE OR REPLACE view is_suivi_commande AS (
                SELECT 
                    sol.id,
                    so.partner_id,
                    sol.product_id,
                    pt.is_famille_id,
                    pt.is_emplacement_stock,
                    so.client_order_ref,
                    sol.product_uom_qty,
                    sol.price_unit,
                    ppl.currency_id,
                    -- so.requested_date,
                    so.commitment_date,
                    to_char(so.commitment_date,'YYYY-MM') as commitment_month,
                    -- is_shipped_qty(pp.id, so.id) as shipped_qty,
                    -- (sol.product_uom_qty-is_shipped_qty(pp.id, so.id)) as remaining_qty,
                    sol.product_uom_qty*sol.price_unit as forecasted_turn_over,
                    -- is_real_shipment_date(pp.id, so.id) as real_shipment_date,
                    -- sol.price_unit*is_shipped_qty(pp.id, so.id) as turn_over_done,
                    so.name as so,
                    '' as mo,
                    so.state
                FROM sale_order so inner join sale_order_line   sol on so.id=sol.order_id 
                                   inner join product_product    pp on pp.id = sol.product_id
                                   inner join product_template   pt on pt.id = pp.product_tmpl_id
                                   inner join product_pricelist ppl on so.pricelist_id = ppl.id
               )
        """)

