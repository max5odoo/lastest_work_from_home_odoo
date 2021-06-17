from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class Sale_task(models.Model):
    _inherit = 'sale.order'

    so_references = fields.Char('So References: ', readonly=False)

    @api.onchange('partner_id')
    def onchange_amo(self):
        for rec in self:
            print(f"\n\n\n\n\nRess name --------->{rec.partner_id.id}--------------\n\n\n\n\n")
            res_id = rec.partner_id.id
            print(f"\n\n\n\n\nparent  search name --------->{rec.partner_id.parent_id}--------------\n\n\n\n\n")
            parent_record = rec.partner_id.parent_id
            print(f"\n\n\n\n\nchild 1111 search name --------->{parent_record.so_references}--------------\n\n\n\n\n")
            if parent_record and not rec.partner_id.so_references:
                rec.write({'so_references': parent_record.so_references})
            else:
                rec.write({'so_references': rec.partner_id.so_references})

    #
    def _prepare_invoice(self):

        a = super(Sale_task, self)._prepare_invoice()
        a.update({
            'so_references': self.so_references
        })

        print(f"\n\n\n\n\n{a}\n\n\n\n\n")
        return a
43

class Customer_task(models.Model):
    _inherit = 'res.partner'

    so_references = fields.Char('So References: ')


class Invoice_task(models.Model):
    _inherit = 'account.move'

    so_references = fields.Char('So References: ', readonly=False)

    @api.onchange('partner_id')
    def onchange_invoice(self):
        for rec in self:
            print(f"\n\n\n\n\nRess name --------->{rec.partner_id.id}--------------\n\n\n\n\n")
            res_id = rec.partner_id.id
            print(f"\n\n\n\n\nparent  search name --------->{rec.partner_id.parent_id}--------------\n\n\n\n\n")
            parent_record = rec.partner_id.parent_id
            print(f"\n\n\n\n\nchild 1111 search name --------->{parent_record.so_references}--------------\n\n\n\n\n")
            if parent_record and not rec.partner_id.so_references:
                rec.write({'so_references': parent_record.so_references})
            else:
                rec.write({'so_references': rec.partner_id.so_references})
