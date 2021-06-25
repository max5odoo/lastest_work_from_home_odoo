from odoo import api, models, fields


class StudentMailTemplateWizard(models.TransientModel):
    _name = "school.student.mail.wizard"

    email_to = fields.Char()
    subject = fields.Char('Subject')
    body = fields.Html('Contents',sanitize_style=True)
    attachment_ids = fields.Many2many(
        'ir.attachment', 'student_mail_ir_attachments_rel',
        'wizard_id', 'attachment_id', 'Attachments')
    stu_id = fields.Many2one('school.student.detail',default = lambda self : self.env['school.student.detail'].browse(self._context.get("active_id")))    

    def action_send_mail(self):
        print(f"\n\n\n active id of student : {self.stu_id} \n\n\n")
        email_values = {'email_to' : self.email_to , 'subject' : self.subject,'body' : self.body,'attachment_ids':[(4, attach.id)  for attach in self.attachment_ids]}
        mail_template = self.env.ref('new_app.student_email_template')
        mail_template.send_mail(self.id, email_values = email_values , force_send=True)
        print("\n\n\n mail successfully sent... \n\n\n")

