from odoo import models, fields, api


class TaskCreationReportWizard(models.TransientModel):
    _name = 'task.creation.report.wizard'
    _inherit = 'tasks.tasks'

    tasks_id = fields.One2many('tasks.tasks', 'student_id', string='Task names')
    # task_name = fields.Char(string='Task Name')
    # task_technology = fields.Char(string='Task Technology Used')
    task_new_id = fields.Many2many('tasks.tasks', 'task_task_wizard', 'wiz_id', 'task_id', string='tasks')

    # def set_data(self):
    #     fees = self.env['student.student'].browse(s
    #         self._context.get("active_id")).read(['task_name'])
    #     print(f"n\n\n {fees} \n\n\n")
    #     new_fees = fees[0]['task_name']
    #     return new_fees

    # this is a wizard function ('ama apde potana student ni one2many ma create thai jay record---------particularly same student ma ')
    def create_new_button(self):
        events = self.env['student.student'].browse(self._context.get("active_id"))
        print(f"\n\nstudent normal - - {events}\n\n\n")
        student_data = events.write({
            'tasks_id': [(5, 0, 0), (0, 0, {
                'task_name': self.task_name,
                'task_technology': self.task_technology
            })]
        })
        print(f"\n\nstudent data- - {student_data}\n\n\n")
        return student_data

    # this is a wizard function ('ama apde potana student  (4,id) use karyu che ni one2many ma create thai jay record---------particularly same student ma ')
    # def create_new_button(self):
    #     new_task_ids = self.task_new_id
    #     print(f"n\n\n {new_task_ids} \n\n\n")
    #     for i in range(len(new_task_ids)):
    #         events = self.env['student.student'].browse(self._context.get("active_id"))
    #         print(f"\n\nstudent normal - - {events}\n\n\n")
    #         student_data = events.write({
    #             'tasks_id': [(4, new_task_ids[i].id)]
    #         })


class TaskMailWizard(models.TransientModel):
    _name = 'task.mail.report.wizard'
    activity_type_id = fields.Many2one(
        'mail.activity.type', string='Activity Type', readonly=True,
        default=lambda self: self.env['mail.activity.type'].search([('name', '=', 'To Do')])
    )
    summary = fields.Char('Summary')
    date_deadline = fields.Date('Due Date', index=True, default=fields.Date.context_today)
    user_id = fields.Many2one(
        'res.users', 'Assigned to',
        default=lambda self: self.env.user,
        index=True)

    def create_new_button(self):
        print(f"n\n\n context male:----{self.env.context} \n\n\n")
        data_res = self.env['ir.model'].search([('model', '=', self.env.context.get('active_model'))])
        print(f"n\n\n res data:----{data_res.model} \n\n\n")
        student_data = self.env['mail.activity'].create({
            'res_id': self.env.context.get('active_id'),
            'res_model_id': data_res.id,
            'activity_type_id': self.activity_type_id.id,
            'summary': self.summary,
            'date_deadline': self.date_deadline,
        })
        print(f"\n\nstudent - - {student_data}\n\n\n")
        return student_data


class TasksetvalueWizard(models.TransientModel):
    _inherit = 'res.config.settings'

    template_id_new = fields.Many2one('mail.template', 'Email')

    @api.model
    def get_values(self):
        res = super(TasksetvalueWizard, self).get_values()
        res['template_id_new'] = int(self.env['ir.config_parameter'].sudo().get_param('template_id_new'))
        print(f"\n\nResss _____>{res['template_id_new']}\n\n\n")
        return res

    @api.model
    def set_values(self):
        rest_set = super(TasksetvalueWizard, self).set_values()
        res_get = self.env['ir.config_parameter'].sudo().set_param(
            'template_id_new', self.template_id_new.id)
        print(f"\n\nResss sett_____>{res_get}\n\n\n")


class TaskMailSendingWizard(models.TransientModel):
    _name = 'task.mail.sending.wizard'

    email_to = fields.Char()
    subject = fields.Char('subject')
    student_body = fields.Html('Contents')
    stu_id = fields.Many2one('student.student',
                             default=lambda self: self.env['student.student'].browse(self._context.get("active_id")))
    student_ids = fields.Many2many('student.student', 'student_student_tasks',
                                   'student_ids', 'tasks_ids', string='student tasks')
    attachment_ids = fields.Many2many(
        'ir.attachment', 'student_mail_ir_attachments_rel',
        'wizard_id', 'attachment_id', 'Attachments')

    def send_email_button(self):
        for rec in self:
            template_id = self.env.ref('manthan.student_sending_email_templates')
        if template_id:
            print("mail template yess")
            print(f"self.env['student.student'].browse([stu.id]).student_email")
            for stu in rec.student_ids:
                email_valuess = {'email_to': self.env['student.student'].browse([stu.id]).student_email,
                                 'subject': rec.subject,
                                 'body_html': rec.student_body,
                                 'attachment_ids': [(4, attach.id) for attach in self.attachment_ids]}
                print("mail values yess")
                print(f"\n\n\n\n\n\n{email_valuess}\n\n\n\n\n\n")
                print(
                    f"\n\n\n\n\n\nthis is the email ---->{self.env['student.student'].browse([stu.id]).student_email}\n\n\n\n\n\n")
                template_id.send_mail(
                    stu.id, email_values=email_valuess, force_send=True)
        else:
            print("mail is not send")

# [(5, 0, 0), (0, 0, { 'student_body': 'stu.student_email' })],   <<<<<<<<<<<<<-------------this is to put in the email_body
