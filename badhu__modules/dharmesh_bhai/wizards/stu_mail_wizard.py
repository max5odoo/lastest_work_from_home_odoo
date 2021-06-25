from odoo import models, fields, api
from datetime import date


class StudentMailWizard(models.TransientModel):
    _name = "student.mail.wizard"
    _description = "this is student mail wizard model"

    mail_to = fields.Many2many("student.data")
    email_data_wizard = fields.Html('Data of student', sanitize_style=True)
    subject_msg = fields.Char(max_length=30)
    attechment_ids = fields.Many2many(
        'ir.attachment', 'student_attch', 'ir_attach_id', 'student_id')

    def Send_mail_user(self):
        print("\n\n\n\n mail\n\n\n\n",
              self.mail_to.first_name)

        for rec in self:
            for stu in rec.mail_to:

                template_id = self.env.ref('student_app.dh_email_template')
                # just remember method serch/ rec.mail_to = self.env['student.data'].browse([stu.id]).email

                email_values = {'email_to': self.env['student.data'].browse([stu.id]).email, 'subject': self.subject_msg, 'attachment_ids': [
                    (4, dt.id) for dt in self.attechment_ids], 'body_html': rec.email_data_wizard}
                print("\n\n\n\n mail\n\n\n\n",
                      email_values)
                template_id.send_mail(
                    stu.id, email_values=email_values, force_send=True)

        # ----------method2 send mail direct button------------
        # template_id = self.env.ref('student_app.dh_email_template').id
        # self.env['mail.template'].browse(template_id).send_mail(
        #     self.id, force_send=True)
