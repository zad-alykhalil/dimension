from odoo import fields, models, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    invoice_dimension = fields.Char(string="Dimension", store=True, readonly=True, )


class AccountMove(models.Model):
    _inherit = 'account.move'
