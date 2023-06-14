from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    sale_dimension = fields.Char(string="Dimension", required=False, )

    @api.model
    def _prepare_procurement_values(self, group_id=False):
        res = super(SaleOrderLine, self)._prepare_procurement_values(group_id=group_id)
        res.update({'stock_dimension': self.sale_dimension})
        return res


class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id,
                               values):
        move_values = super()._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin,
                                                     company_id, values)
        if values.get('stock_dimension'):
            move_values['stock_dimension'] = values['stock_dimension']
        return move_values

    def _prepare_invoice_line(self, **optional_values):
        res = super(StockRule, self)._prepare_invoice_line()
        res.update({
            'invoice_dimension': self.move_ids.stock_dimension
        })
        return res