from odoo import models, fields, api


class TaskMailSendingWizard(models.TransientModel):
    _name = 'task.mail.sending.wizard'

    email_to = fields.Char()
    subject = fields.Char('subject')
    student_body = fields.Html('Contents')
    stu_id = fields.Many2one('school.student.detail',
                             default=lambda self: self.env['school.student.detail'].browse(self._context.get("active_id")))
    student_ids = fields.Many2many('school.student.detail', 'student_student_courses',
                                   'student_id', 'course_id', string='student courses')
    attachment_ids = fields.Many2many(
        'ir.attachment', 'student_mail_ir_attachments_rel_new',
        'wizard_id', 'attachment_id', 'Attachments')

    def send_email_button(self):
        for rec in self:
            template_id = self.env.ref(
                'dhruv_main.student_sending_email_template_pc ')
            print(f"\n\n\n {template_id} \n\n\n")
        if template_id:
            for stu in rec.student_ids:
                email_valuess = {'email_to': self.env['school.student.detail'].browse([stu.id]).email_id,
                                 'body_html': rec.student_body,
                                 # 'body': rec.student_body,
                                 'attachment_ids': [(4, attach.id) for attach in self.attachment_ids]}
                print(f"\n\n\n\n\n\n{email_valuess}\n\n\n\n\n\n")
                template_id.send_mail(
                    stu.id, email_values=email_valuess, force_send=True)
