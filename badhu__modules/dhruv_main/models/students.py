from odoo import models, fields, api, _
from datetime import datetime
from odoo.tools.misc import xlsxwriter
import io
import xlrd
import sys

from odoo.exceptions import UserError, ValidationError


sys.setrecursionlimit(2000)


class Students(models.Model):
    _name = "school.student.detail"
    _description = "student detail"
    _order = "email_id DESC"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    # _inherit = ["todos.detail"]

    name = fields.Char(string='Name', required=True, tracking=3)
    avatar_img = fields.Image(max_width=25, max_height=25)
    email_id = fields.Char(string='Email', default='manthan@gmail.com',)
    todo_name = fields.Many2one(
        'todos.detail', string="Todo", ondelete="cascade")
    is_completed = fields.Boolean(
        related='todo_name.is_done', string="Is Completed")
    address_line1 = fields.Char(string='Address Line1', copy=True)
    address_line2 = fields.Char(string='Address Line2')
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ], 'Gender', default='male')
    fees = fields.Float(string='Fees', digits=(12, 6))
    # course_li_ids = fields.One2many(
    #     'courses.detail', 'st_id', string='Course Lines')
    skill_per = fields.Integer(string="Skill Per.", default=70)
    max_skill_per = fields.Integer(default=70)
    course_tags = fields.Many2many(
        'courses.detail', 'student_course_rel', 'student_id', 'course_id', string='Courses')
    course_payment_status = fields.Selection(
        [('ordered', 'Ordered'), ('pending', 'Pending'), ('delivered', 'Delivered')])
    course_cnt = fields.Integer('Courses', compute='get_course_doc_cnt')
    course_ids = fields.One2many(
        'course.data.lines', 'st_id', string='Course Lines')
    login_user = fields.Many2one(
        'res.users', default=lambda self: self.env.user)
    password = fields.Char()
    signature = fields.Binary(max_width=50, max_height=50)

    def get_course_doc_cnt(self):
        for rec in self:
            # print(f"\n\n\n courses search count :
            # {self.env['course.data.lines'].search_count([('st_id', '=',
            # self.id)])} \n\n\n")
            rec.course_cnt = self.env['course.data.lines'].search_count(
                [('st_id', '=', rec.id)])  # st_id (course_) - rec.id - student  - 4

    # _sql_constraints = [

    #     ('skill_per_check', 'CHECK((skill_per >= 65 ))',
    #      'Skill Per. must be >= 65.'),
    #     ('max_skill_per_check', 'CHECK((max_skill_per >= 55 ))',
    #      'Max Skill Per. must be >= 55.'),
    # ]

    def test_cron_func(self):
        print("\n\n\nsuccessfully called test_cron_func()... :) \n\n\n")

    def add_new(self):
        vals = {
            'name': 'Maxw_e',
            'email_id': 'maxw_e@gmail.com',
            'gender': 'male'
        }
        stu_rec = super(Students, self).create(vals)
        print(f"\n\n\n record added successfully of {stu_rec}  :) \n\n\n")

    @api.model
    def create(self, vals):
        # set default val if email_id ""
        if not vals["email_id"]:
            print("\n\n\n email id is '' \n\n\n")
            default_email_id = super(Students, self).default_get(['email_id'])
            vals.update({'email_id': default_email_id['email_id']})
        return super(Students, self).create(vals)

    # #(4,ID) - for one2many,many2many
    # @api.model
    # def create(self, vals):
    #     print(f"\n\n\n student input dt : {vals}\n\n\n")
    #     print(f"\n\n\n\n xml record id {self.env.ref('dhruv_main.course_data_3').id} \n\n\n")
    #     vals.update({'course_li_ids': [(4, self.env.ref('dhruv_main.course_data_3').id)],
    #                  'course_tags': [(4, self.env.ref('dhruv_main.course_data_2').id)]})
    #     # student_obj = super(Students, self).create({
    #     #     # 'name': vals['name'],
    #     #     # 'email_id': vals['email_id'],
    #     #     'address_line1': vals['address_line1'],
    #     #     'course_li_ids': [(4, self.env.ref('dhruv_main.course_data_3').id)],
    #     #     'course_tags': [(4, self.env.ref('dhruv_main.course_data_2').id)]

    #     # })
    #     # print(f"\n\n\n student input dt : {vals}\n\n\n")
    #     res = super(Students, self).create(vals)
    #     return res
    #     # return student_obj

    # #(4,ID) - for one2many
    # def write(self, vals):
    #     vals['name'] = 'GKT'
    #     # professor_obj = super(Professors, self).search([])
    #     print(f"\n\n\n before : {vals['email_id']} \n\n\n")
    #     vals["email_id"] = (super(Students, self).default_get(["email_id"]))[
    #         "email_id"]
    #     print(f"\n\n\n before : {vals['email_id']} \n\n\n")
    #     student_obj = super(Students, self).write({
    #         'name': vals['name'],
    #         'email_id': vals['email_id'],
    #         'course_li_ids': [(4, self.env.ref('dhruv_main.course_data_3').id)]
    #     })
    #     print(f"\n\n\n student input dt : {vals}\n\n\n")
    #     return student_obj

    # (6,0,ID) - for many2many
    # def write(self, vals):
    #     vals['name'] = 'AKA'
    #     # professor_obj = super(Professors, self).search([])
    #     student_obj = super(Students, self).write({
    #         'name': vals['name'],
    #         'course_tags': [(6, 0, [self.env.ref('dhruv_main.course_data_1').id, self.env.ref('dhruv_main.course_data_2').id])]
    #     })
    #     print(f"\n\n\n student input dt : {vals}\n\n\n")
    #     return student_obj

    #  #(5,0,0) - for one2many
    # def write(self, vals):
    #     vals['name'] = 'JKT'
    #     # professor_obj = super(Professors, self).search([])
    #     student_obj = super(Students, self).write({
    #         'name': vals['name'],
    #         'course_li_ids': [(5, 0, 0)]
    #     })
    #     print(f"\n\n\n student input dt : {vals}\n\n\n")
    #     return student_obj

    # #(5,0,0) - for many2many
    # def write(self, vals):
    #     vals['name'] = 'SKT'
    #     # professor_obj = super(Professors, self).search([])
    #     student_obj = super(Students, self).write({
    #         'name': vals['name'],
    #         'course_tags': [(5, 0, 0)]
    #     })
    #     print(f"\n\n\n student input dt : {vals}\n\n\n")
    #     return student_obj

    # @api.onchange('email_id')
    # def change_email(self):
    #     for rec in self:
    #         record = super(Students, self).default_get(['email_id'])
    #         rec.email_id = record['email_id']

    def action_ordered(self):
        for rec in self:
            if rec.course_li_ids.id:
                print("staus changed to 'ordered'.")
                rec.write({'course_payment_status': 'ordered'})

    def action_pending(self):
        for rec in self:
            if rec.course_li_ids.id:
                print("staus changed to 'pending'.")
                if rec.course_payment_status == 'ordered':
                    rec.write({'course_payment_status': 'pending'})

    def action_delivered(self):
        for rec in self:
            if rec.course_li_ids.id:
                print("staus changed to 'delivered'.")
                if rec.course_payment_status == 'pending':
                    rec.write({'course_payment_status': 'delivered'})

    def action_course(self):
        # self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Courses',
            'view_mode': 'tree,form',
            'res_model': 'course.data.lines',
            'domain': [('st_id', '=', self.id)],
        }

    def open_wizard(self):

        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'school.student.fees.wizard',
            'target': 'new'
        }

    def open_mail_template_wizard(self):

        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'school.student.mail.wizard',
            'target': 'new'
        }

    def open_mail_template_wizard_m2m(self):

        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'task.mail.sending.wizard',
            'target': 'new'
        }

    def send_mail(self):
        mail_template = self.env.ref('new_app.student_email_template_u')
        mail_template.send_mail(self.id, force_send=True)
        # print("\n\n\n mail sent successfully... \n\n\n")

    def export_all_record_xl_report(self):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook('E:/students.xlsx')
        worksheet = workbook.add_worksheet()

        bold = workbook.add_format({'bold': True})

        # for header
        worksheet.write(0, 0, "Name", bold)
        worksheet.write(0, 1, "Gender", bold)
        worksheet.write(0, 2, "Email", bold)

        students = self.env['school.student.detail'].search([])
        print(f"\n\n\n students rec  : {students}  \n\n\n")
        row = 1

        # for vals
        for student in students:
            print(f"\n\n\n student rec  : {student}  \n\n\n")
            worksheet.write(row, 0, student.name)
            worksheet.write(row, 1, student.gender)
            worksheet.write(row, 2, student.email_id)
            row += 1
        print("\n\n\n all record exported successfully... \n\n\n")
        workbook.close()
        return workbook

    def export_c_record_xl_report(self):
        for rec in self:
            file_name = f'E:/{rec.name}.xlsx'
            workbook = xlsxwriter.Workbook(file_name)
            worksheet = workbook.add_worksheet()

            bold = workbook.add_format({'bold': True})

            # for header
            worksheet.write(0, 0, "Name", bold)
            worksheet.write(0, 1, "Gender", bold)
            worksheet.write(0, 2, "Email", bold)

            students = self.env['school.student.detail'].search(
                [('id', '=', rec.id)])
            print(f"\n\n\n students rec  : {students}  \n\n\n")
            row = 1

            # for vals
            for student in students:
                print(f"\n\n\n student rec  : {student}  \n\n\n")
                worksheet.write(row, 0, student.name)
                worksheet.write(row, 1, student.gender)
                worksheet.write(row, 2, student.email_id)
                row += 1
            print("\n\n\n current record exported successfully... \n\n\n")
            workbook.close()
            return workbook

    def send_msg(self, message=None):
        print("\n\n\n msg send successfully... \n\n\n")
        attachment = self.env['ir.attachment'].create({
            'datas': self.avatar_img,
            'name': 'students.png',
            'res_model': 'mail.compose.message',
        })
        return self.message_post(
            body='Hello Devs...  👌😂👌',
            subject='Greetings',
            author_id=self.env.user.id,
            message_type='email',  # notification,,
            attachment_ids=[attachment.id]
        )

    def validate_emailid(self):
        for rec in self:
            if not rec.email_id:
                raise ValidationError("Please enter email id")


class CourseStudentline(models.Model):
    _name = 'course.data.lines'

    course_id = fields.Many2one(
        'courses.detail', ondelete="set default", required=True)
    st_id = fields.Many2one('school.student.detail')
    short_desc = fields.Char(string="Short Desc.",
                             related='course_id.short_desc')
    created_by = fields.Char(
        string="Created By", related='course_id.created_by')

    def name_get(self):
        label = []
        for rec in self:
            title = f"{rec.course_id.name} ({rec.st_id.name})"
            label.append((rec.id, title))
        return label


class SchoolStudentUpdate(models.Model):
    _inherit = 'school.student.detail'

    course_payment_status = fields.Selection(
        selection_add=[('ordered', 'Ordered'),
                       ('rejected', 'Rejected'),
                       ('pending', 'Pending'),
                       ('delivered', 'Delivered')])
