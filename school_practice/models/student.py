import xlrd
import xlsxwriter

from odoo import fields, models, api


class Student(models.Model):
    _name = 'student.details'
    _description = 'This is the student class'
    _rec_name = 'first_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    first_name = fields.Char(default='maxy')
    last_name = fields.Char(default='chawda', copy=False)
    email = fields.Char()
    mobile_no = fields.Integer()
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ], 'Gender', default='male')
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
        ('3', 'Very High'),
    ])
    profile_pic = fields.Image()
    address = fields.Text()
    dob = fields.Date()
    age = fields.Integer()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('cancelled', 'Cancelled'),
    ], default='draft', string='State')
    xls_file = fields.Binary('File')

    # ---------------------------------------------------------------------------------SalePaymentLink------------
    # BELOW IS THE DRAFT STATE BUTTON
    def button_draft(self):
        for record in self:
            record.state = 'draft'

    # BELOW IS THE CONFIRM STATE BUTTON
    def button_confirm(self):
        for rec in self:
            rec.write({'state': 'confirm'})

    # BELOW IS THE CANCELLED STATE BUTTON
    def button_cancel(self):
        for rec in self:
            rec.write({
                'state': 'cancelled'
            })

    # BELOW IS THE EMAIL CHANGE BUTTON IN  OE_BUTTON_BOX
    def button_email_change(self):
        for rec in self:
            rec.write({
                'email': 'manthan.chawda05@gmail.com',
                'age': 20
            })

    # ---------------------------------------------------------------------------------------------
    # BELOW IS THE LOG NOTE BUTTON IN HEADER
    def log_note(self):
        for rec in self:
            return rec.message_post(
                body='Hii here is MANTHAN CHAWDA',
                subject='Just Testing',
                author_id=self.env.user.id,
            )

    # ---------------------------------------------------------------------------------------------
    # THIS IS THE COPY METHODS
    # def copy(self, default={}):
    #     self.ensure_one()
    #     print(f"\n\n\nSELF--->>>{self.last_name}<<<---\n\n\n")
    #     print(f"\n\n\nDEFAULT--->>>{default}<<<---\n\n\n")
    #     default['last_name'] = ''
    #     return super(Student, self).copy(default=default)

    # ---------------------------------------------------------------------------------------------
    # THIS IS THE DEFAULT_GET METHOD
    @api.model
    def default_get(self, fields):
        res = super(Student, self).default_get(fields)
        print(f'\n\n\n\nThis is the res----->{res}\n\n\n\n')
        return res

    # ---------------------------------------------------------------------------------------------
    # BELOW CODE IS FOR EXPORT THE RECORD
    def student_xlsx(self):
        workbook = xlsxwriter.Workbook('maxy.xlsx')
        worksheet = workbook.add_worksheet('manthan')
        header_bold = workbook.add_format({'bold': True, 'pattern': 1, 'bg_color': '#AAAAAA'})
        student_records = self.env['student.details'].search([])
        print(f'\n\n\n\n{student_records}\n\n\n')
        worksheet.write(0, 0, 'first_name', header_bold)
        worksheet.write(0, 1, 'last_name', header_bold)
        worksheet.write(0, 2, 'email', header_bold)
        worksheet.write(0, 3, 'mobile_no', header_bold)
        row = 1
        col = 0
        for key in student_records:
            print(f'\n\n\n\n this is key{key}\n\n\n')
            worksheet.write(row, col, key.first_name)
            worksheet.write(row, 1, key.last_name)
            worksheet.write(row, 2, key.email)
            worksheet.write(row, 3, key.mobile_no)
            row += 1

        workbook.close()

        return workbook

    # ----------------------------------------------------------------------------------------------------
    def student_xlrd(self):
        wb = xlrd.open_workbook('maxy.xlsx')
        for sheet in wb.sheets():
            for row in range(sheet.nrows):
                for col in range(sheet.ncols):
                    student_read = sheet.cell(row, col).value
                    student_record = self.env['student.details'].create({
                        'first_name': student_read
                    })

                    print(student_read)

    # -----------------------------------------------------------------------------------------------------------
