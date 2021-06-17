from odoo import models, fields, api


class SaleOrderModel(models.Model):
    _inherit = 'sale.order'

    so_reference = fields.Char()

    # @api.depends('partner_id')
    # def change_soref(self):
    #   for rec in self:
    #       # print(f"\n\n\n {rec.partner_id.name} \n\n\n")
    #       # contact_rec = self.env['res.partner'].browse([rec.partner_id.id])
    #       # print(f"\n\n\n {contact_rec.so_reference} \n\n\n")
    #       if not rec.partner_id.so_reference:
    #           rec.so_reference = ""
    #       else:
    #           rec.so_reference = rec.partner_id.so_reference

    @api.onchange('partner_id')
    def change_sale_soref(self):
        
        for rec in self:
            #by company_type
            # company_type = rec.partner_id.company_type 
            # if company_type == "person" and not rec.partner_id.so_reference:
            #     rec.so_reference = rec.partner_id.parent_id.so_reference
            # else:
            #     rec.so_reference = rec.partner_id.so_reference
            #by is_company  
            is_company = rec.partner_id.is_company
            if not is_company and not rec.partner_id.so_reference:
                rec.so_reference = rec.partner_id.parent_id.so_reference
            else:
                rec.so_reference = rec.partner_id.so_reference
            #by finding 
                

    def _prepare_invoice(self):
        invoice_dt = super(SaleOrderModel,self)._prepare_invoice()
        print(f"\n\n\n {invoice_dt}  \n\n\n")
        return invoice_dt

        
                


                


class CustomerModel(models.Model):
    _inherit = 'res.partner'

    so_reference = fields.Char()
    designation = fields.Selection(
        [('student', 'Student'), ('professor', 'Professor')], 'Designation',default='student')
    




class InvoiceModel(models.Model):
    _inherit = 'account.move'

    so_reference = fields.Char()

    @api.onchange('partner_id')
    def change_sale_soref(self):
        
        for rec in self:
            #by company_type
            # company_type = rec.partner_id.company_type 
            # if company_type == "person" and not rec.partner_id.so_reference:
            #     rec.so_reference = rec.partner_id.parent_id.so_reference
            # else:
            #     rec.so_reference = rec.partner_id.so_reference
            #by is_company  
            is_company = rec.partner_id.is_company
            if not is_company and not rec.partner_id.so_reference:
                rec.so_reference = rec.partner_id.parent_id.so_reference
            else:
                rec.so_reference = rec.partner_id.so_reference                

