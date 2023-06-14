from odoo import fields, models, api


class StockMove(models.Model):
    _inherit = 'stock.move'

    stock_dimension = fields.Char(string="Dimension",  store=True, readonly=False, )
