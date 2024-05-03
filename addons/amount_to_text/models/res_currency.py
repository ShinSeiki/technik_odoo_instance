# -*- encoding: utf-8 -*-

from odoo import api, fields, models, _
from . import amount_to_text_es

class Currency(models.Model):
    _inherit = 'res.currency'
    
    singular_name = fields.Char("Singular Name")
    plural_name = fields.Char("Plural Name")
    fraction_name = fields.Char("Faction Name")
    show_fraction = fields.Boolean("Show Fraction")
    
    ##@api.multi
    def amount_to_text(self, amount):
        self.ensure_one()
        if amount<2 and amount>=1:
                currency = self.singular_name or self.plural_name or self.name or ""
        else:
            currency = self.plural_name or self.name or ""
        sufijo = self.fraction_name or ""
        amount_text = amount_to_text_es.amount_to_text(amount, currency, sufijo, self.show_fraction) 
        return amount_text