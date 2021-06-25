from odoo import fields, models, api
from odoo.exceptions import ValidationError


class SaleReport(models.TransientModel):
    _name = 'sale.report.wizard'
    _description = 'sale.report.wizard'

    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date('End Date', required=True)

    def print_report(self):
        if self.end_date>self.start_date:
            data = {
                'model': 'sale.report.wizard',
                'form': self.read()[0]
            }
            orders = self.env['sale.order'].search([('date_order', '>=', self.start_date),
                                                    ('date_order', '<=', self.end_date)])

            sale_records = [{'name': order.name,
                             'date_order': order.date_order.date(),
                             'partner_id': order.partner_id.name,
                             'amount_total': order.amount_total,
                             'state': order.state,
                             } for order in orders]

            records = len(sale_records)
            if records > 0:
                return self.env.ref('wizard_report_sale.sale_wiz_report_1').report_action(self, data={
                    'order_list': sale_records,
                    'all_amount_total': sum([order.amount_total for order in orders]),
                    'start_date': self.start_date,
                    'end_date': self.end_date,
                    'counter': len(sale_records),
                })
            else:
                raise ValidationError(f"There is No orders between {self.start_date} and {self.end_date}")

        else:
            raise ValidationError("Starting Date must be less than Ending Date.")


