from doc._extensions.pyjsparser.parser import true
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.tools import get_lang


class GroupInvoice(models.TransientModel):
    _inherit = "account.invoice.send"

    #
    @api.onchange('invoice_ids')
    def _compute_composition_mode(self):
        print("\n\n\n\n\n<--this is the multi called--->\n\n\n\n")
        for wizard in self:
            wizard.composer_id.composition_mode = 'comment'

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        if self._context.get('active_model') == 'account.move':
            lines = self.env['account.move'].browse(self._context.get('active_ids', []))
            if len(lines) > 100:
                raise UserError(_("You have more than 100 invoices selected"))
            for line in lines:
                if lines[0].partner_id.name != line.partner_id.name:
                    raise UserError(_("You have same name of invoices"))
            return res

    def _print_document(self):
        self.ensure_one()
        action = self.invoice_ids.action_invoice_print()
        action.update({'close_on_report_download': True})
        return action


class AccountNewMove(models.Model):
    _inherit = "account.move"

    def action_invoice_print(self):
        if any(not move.is_invoice(include_receipts=True) for move in self):
            raise UserError(_("Only invoices could be printed."))

        self.filtered(lambda inv: not inv.is_move_sent).write({'is_move_sent': True})
        if self.user_has_groups('account.group_account_invoice'):
            return self.env.ref('much_group_invoice.report_student_info').report_action(self)
