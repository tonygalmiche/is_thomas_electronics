# -*- coding: utf-8 -*-
from odoo import fields, models, api

class mrp_workorder(models.Model):
    _inherit = "mrp.workorder"

    @api.depends('duration_expected')
    def _compute_is_duration_expected_heure(self):
        for obj in self:
            obj.is_duration_expected_heure = obj.duration_expected/60.0

    is_duration_expected_heure = fields.Float(string='Durée attendue (H)', compute='_compute_is_duration_expected_heure')



