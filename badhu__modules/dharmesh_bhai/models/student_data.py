from operator import index
from odoo import api
from odoo.tools.misc import unique
# from odoo.api import model, onchange
from random import choices
from odoo import models, fields, _
from odoo.exceptions import UserError, ValidationError
import datetime


bd_group = [
    ('a+', 'A+'),
    ('b+', 'B+'),
    ('o', 'O'),
    ('a-', 'A-'),
    ('b-', 'B-'),
    ('ab+', 'AB+'),
    ('ab-', 'AB-'),
]

select_course = []


class student_data(models.Model):
    _name = 'student.data'
    _rec_name = 'first_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    first_name = fields.Char(string='firstname', max_length=30, copy=False)
    last_name = fields.Char(string='lastname', max_length=30,)
    address = fields.Text(max_length=50)
    email = fields.Char(string='your_email', max_length=20)
    password = fields.Char()
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    blood_group = fields.Selection(bd_group)
    age = fields.Integer(string="your age", tracking=True)
    country_code = fields.Integer(max_length=3, copy=False)
    mobile = fields.Integer(max_length=10, tracking=3, copy=False)
    register = fields.Boolean(default=False)
    dates = fields.Date(string="Date of Birth")
    # rdate = fields.Date.today()
    profestion = fields.Selection(
        [('other', 'Other'), ('professor', 'Professor')])
    email_data = fields.Html('Data of student')
    skill_list = fields.Many2many(
        'student.skill', 'student_hobby_relf', 'studenthobby_idd', 'hobby_idd')
    handle = fields.Integer()
    # res_id = fields.Many2one(
    #     'res.partner', string="Student")
    photo_id = fields.Binary()
    student_line_ids = fields.One2many('student.data.lines', 'stu_id')
    state = fields.Selection(
        [('pending', 'Pending'), ('confirm', 'Confirm'),
         ('paid', 'Paid'), ('cancel', 'Cancel')], tracking=True)
    course_count = fields.Integer(compute="course_select_count")
    login_user = fields.Many2one(
        'res.users', default=lambda self: self.env.user)
    signature_by = fields.Char()
    signature = fields.Binary()
    
       
    # login_user = fields.Many2one(
    #     'res.users')
    # report_template = fields.Html()

    _sql_constraints = [
        ('unique_mail',
         'unique(email)',
         'email must be unique'),
        # ('bom_qty_zero', 'CHECK (age >=18)',
        #  'All product quantities must be greater or equal to 0.'),
        ('check_age',
         'CHECK(age>20 AND age<60)',  # if any condtion False Then Raise Error
         'check age must beetween 20 and 60'),

        ('unique_phone_cons',
         'unique(mobile)',
         'phone must be unique'),


    ]

    # security = fields.Text(groups='base.group_system')
    # @api.constrains('last_name')
    # def last_name_email_compulsory(self):
    #     print(f'\n\n\n\n{self.last_name}\n\n\n\n\n')
    #     for rec in self:
    #         if not rec.last_name:
    #             raise ValidationError("last name must be enter..")

   

    def name_get(self):
        result = []
        for field in self:
            # print(f'\n\ncheck forloop dharmesh  {self} \n\n')\
            # check forloop dharmesh  student.data(1,)
            result.append((field.id, "{} {}".format
                           (field.first_name, field.last_name)))
            # print(f'\n\ncheck forloop dharmesh  {result} \n\n')
            # check forloop dharmesh  [(1, 'sivam khachiya')]
        return result

    @api.onchange('student_line_ids')
    def onchange_add_course(self):
        print("\n\n selfffff =>", self)
        for student in self:
            print("\n\n line ==>", student.student_line_ids)
            if len(student.student_line_ids) > 0:
                student.write({'state': 'pending'})
            else:
                student.write({'state': ''})

    @api.onchange('dates')
    def onchange_dob(self):
        for rec in self:
            if rec.dates:
                val1 = rec.dates
                print(f"\n\n\n\nhi dharmesh your age{val1}\n\n\n\n")
                val2 = datetime.date.today()
                # print(f"\n\n\n\nhi dharmesh your ageval2{val2}\n\n\n\n")
                rec.age = abs(((val2 - val1).days)//365)

    def Send_mail_direct(self):
        template_id = self.env.ref('student_app.dh_email_template_direct')
        print("\n\n\n\n mail dhmaaaaaaaaaa\n\n\n\n")
        print(template_id)
        template_id.send_mail(
            self.id, force_send=True)

    def id6_test_action(self):
        print("\n\n\n\nid6\n\n\n\n")
        for rec in self:
            dt = self.env["student.skill"].browse([4, 1])
            rec.skill_list = [(6, 0, [dts.id for dts in dt])]
            # rec.skill_list = [(5, 0, 0)]

    def id_test_action(self):
        # data = super(student_data, self).default_get(fields)
        print("\n\n\n\n\n4,id\n\n\n\n\n")
        for rec in self:
            # (4,id,0) conecpt many2many field
            # dt = self.env["student.skill"].browse([2, 3, 4])
            # for dta in dt:
            #     rec.skill_list = [(4, dta.id, 0)]
            # print(dt.name)

            # rec.student_line_ids = [(5, 0, 0)]
            # (4,id,0) conecpt many2many field
            dt = self.env["student.data.lines"].browse([2])
            rec.student_line_ids = [(4, dt.id, 0)]

    def action_confirm(self):
        for rec in self:
            if rec.student_line_ids.course_id:
                # print(f"\n\n\n\n\nhi confirm{rec}\n\n\n\n\n\n")
                # rec.state = "confirm"     # also direct store dasta to field
                rec.write({'state': 'confirm', 'login_user': self.env.user.id})

    def action_paid(self):
        for rec in self:
            if rec.student_line_ids.course_id:
                # print(f"\n\n\n\n\nhi paid{rec}\n\n\n\n\n\n")
                rec.write({'state': 'paid'})

    def action_cancel_all(self):
        for rec in self:
            print(f"\n\nhi why cancel\n\n")
            line_cousre = self.env['student.data.lines'].search(
                [('stu_id', '=', rec.id)])
            # write by default work ass for loop
            line_cousre.write({'state': 'cancel'})
            # for course in line_cousre:
            #     course.course_cancel = False
            #     rec.write()

            #     self.env["courses.data"].search(
            #     [('course_names', '=', 'python')])
            # print(f"\n\n\n\n\n{line_cousre}\n\n\n\n\n\n")

    def action_cancel(self):
        for rec in self:

            print(f"\n\n\n\n\nhi why cancel\n\n\n\n\n\n")
            # rec.student_line_ids.cancel_reason
            return {
                'type': 'ir.actions.act_window',
                'name': 'student.wizard.form',
                'view_mode': 'form',
                'res_model': 'student.wizard',
                'target': 'new',
            }

    @ api.model
    def create(self, vals):
        # ----------------get Config-------------------------
        # secret = self.env['ir.config_parameter'].sudo(
        # ).get_param('database.secret')
        # ----------------end------------------------------------
        # print(f"\n\n\n\n\nhi paid dhamaa create method\n\n\n\n\n\n")
        # print(self.env.user)

        # vals['login_user'] = self.env.user.id

        # -------------------------just check logic on create only

        # vals = {
        #     'student_line_ids': [(0, 0, {
        #         'course_id': self.env.ref('student_app.Course_4').id,
        #         'course_amount': 6000,
        #     })]
        #     }
        data_record = super(student_data, self).create(vals)

        # readdata = self.env["student.data"].search_count(
        # [("first_name", '=', vals["first_name"])])
        # print(f"\n\n\n\n{readdata}\n\n")
        # if readdata:
        #     raise ValidationError("name must be unique..")
        # else:

        #     return data_record
        return data_record
    # method call at time of update

    def write(self, vals):
        print(vals)
        for rec in self:
            readdata = self.env["courses.data"].search([])
            # if readdata:
            # print(f"\n\n\n\n{readdata[0].course_names}\n\n")
            # print(f"\n\n\n\n\nhi dhamesh write method\n\n\n\n\n\n")
            # print(super().write(vals))
            # from multiple record acess perticular record
            # self.env["student.data"].create({"first_name": "manthanbhai"}) cmd
            # print(readdata)
        return super(student_data, self).write(vals)

    def unlink(self):
        for rec in self:
            print("record set delete", self)
            rtn = super(student_data, self).unlink()
            print("return value", rtn)
        return rtn

    def stu_course_view(self):
        for rec in self:
            return {
                'type': 'ir.actions.act_window',
                'name': 'course form student',
                'view_mode': 'tree,form',
                'res_model': 'student.data.lines',
                'domain': [('stu_id', '=', rec.id)],

            }

    def course_select_count(self):
        for rec in self:
            # rec.course_count=10
            rec.course_count = self.env["student.data.lines"].search_count(
                [('stu_id', '=', rec.id)])

    def get_report_base_filename(self):
        print("\n\n\n\nreport name\n\n\n\n")
        self.ensure_one()
        return '%s %s' % (self.state, self.first_name)

    @api.model
    def _schedule_call(self):
        print("\n\n\n\n hi dhamresh calll\n\n\n\n")


class student_data_lines(models.Model):
    _name = "student.data.lines"

    profe = [
        ('kalam', 'Kalam'),
        ('navin', 'Navin'),
        ('sirg', 'Sirg'),

    ]
    course_id = fields.Many2one('courses.data', ondelete="set default")
    stu_id = fields.Many2one('student.data')

    professor_name = fields.Selection(profe)
    course_name = fields.Char(related='course_id.course_names')
    course_lengths = fields.Integer(
        related='course_id.course_length')
    course_amount = fields.Float()
    # sale_id = fields.Many2one('sale.order',)
    # sales_field = fields.Float(related="sale_id.currency_rate")
    cancel_reason = fields.Char(max_length=30)
    course_cancel = fields.Boolean(default="True")
    currncy = fields.Many2one(
        "res.currency", default=lambda self: self.env["res.currency"].search([('name', '=', 'EUR')]))

    def action_cancel(self):
        print(f"\n\n\n\n\nhi dekho cancel\n\n\n\n\n\n")
        for rec in self:
            if rec.course_id:
                print(f"\n\n\n\n\nhi why cancel123\n\n\n\n\n\n")
                return {
                    'type': 'ir.actions.act_window',
                    'name': 'student.wizard.form',
                    'view_mode': 'form',
                    'res_model': 'student.wizard',
                    'target': 'new',

                }

    @api.onchange('course_id')
    def onchange_amount(self):
        for rec in self:

            select_course.append(rec.course_id.id)
            print(
                f"\n\n\n\nyou selecting_course{rec.course_id.course_names}list{select_course}\n\n\n\n")
            if rec.course_id:
                rec.stu_id.state = 'pending'
                self.course_amount = rec.course_id.course_amount
        # print(f"\n\n\n\n {self.course_amount, rec.course_amount,rec.id} \n\n\n\n"
            #   )
