# -*- coding: utf-8 -*-
from odoo import fields, models, api

class mrp_workorder(models.Model):
    _inherit = "mrp.workorder"

    @api.depends('duration_expected')
    def _compute_is_duration_expected_heure(self):
        for obj in self:
            obj.is_duration_expected_heure = obj.duration_expected/60.0

    is_duration_expected_heure = fields.Float(string='Durée attendue (H)', compute='_compute_is_duration_expected_heure')


class is_pointage_heure(models.Model):
    _name = "is.pointage.heure"
    _description = "Pointage des heures"
    _order='date_creation desc'
    _rec_name='date_creation'


    @api.depends('operation_id')
    def _compute_temps_passe_total(self):
        for obj in self:
            tps = 0
            if obj.operation_id:
                lines = self.env['is.pointage.heure'].search([("operation_id","=",obj.operation_id.id)])
                for line in lines:
                    tps+=line.temps_passe
            obj.temps_passe_total = tps


    date_creation     = fields.Datetime("Date", readonly=True, index=True, default=fields.Datetime.now)
    user_id           = fields.Many2one("res.users"     , "Opérateur"           , required=True)
    production_id     = fields.Many2one("mrp.production", "Ordre de fabrication", required=True, domain=[('state','in',['confirmed','progress'])])
    operation_id      = fields.Many2one("mrp.workorder" , "Opération (Phase)"   , required=True, index=True)
    temps_passe       = fields.Float('Temps passé (HH:MM)', required=True)
    temps_passe_total = fields.Float('Temps passé total (HH:MM)', compute='_compute_temps_passe_total')
    temps_prevu       = fields.Float('Temps prévu (HH:MM)', related='operation_id.is_duration_expected_heure')
    commentaire       = fields.Char('Commentaire')


    @api.model
    def create(self, vals):
        res = super(is_pointage_heure, self).create(vals)
        res.operation_id.duration = res.temps_passe_total
        return res


    def write(self, vals):
        res = super(is_pointage_heure, self).write(vals)
        for obj in self:
            obj.operation_id.duration = obj.temps_passe_total
        return res


