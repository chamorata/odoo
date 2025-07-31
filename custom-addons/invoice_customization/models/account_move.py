from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    gross_sale = fields.Monetary(string="Gross Sale", compute="_compute_custom_values")
    vat_amount = fields.Monetary(string="VAT", compute="_compute_custom_values")
    vatable_sale = fields.Monetary(string="VATable Sale", compute="_compute_custom_values")
    sc_pwd_discount = fields.Monetary(string="SC/PWD Discount", compute="_compute_custom_values")
    vat_exempt = fields.Monetary(string="VAT-Exempt Sales", compute="_compute_custom_values")
    zero_rated = fields.Monetary(string="Zero-Rated Sales", compute="_compute_custom_values")
    output_vat = fields.Monetary(string="Output VAT", compute="_compute_custom_values")
    withholding_tax = fields.Monetary(string="Withholding Tax", compute="_compute_custom_values")
    net_total_sales = fields.Monetary(string="Net Total Sales", compute="_compute_custom_values")

    @api.depends('invoice_line_ids', 'amount_total')
    def _compute_custom_values(self):
        for rec in self:
            rec.gross_sale = rec.amount_total
            rec.vat_amount = rec.amount_tax
            rec.vatable_sale = rec.amount_total - rec.amount_tax

            # Example fixed values — these would typically be stored somewhere
            rec.sc_pwd_discount = 2000.00
            rec.output_vat = rec.amount_tax
            rec.vat_exempt = 0.0
            rec.zero_rated = 0.0
            rec.withholding_tax = 1500.00

            rec.net_total_sales = rec.amount_total - rec.withholding_tax
