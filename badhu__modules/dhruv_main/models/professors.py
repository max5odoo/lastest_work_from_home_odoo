from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class Professors(models.Model):
    _name = "school.professor.detail"
    _description = "professor detail"
    # _inherit = 'school.subject.line'

    # photo = fields.Binary(string="Photo")

    sequence = fields.Integer(string='Sequence')

    subject_line_ids = fields.One2many(
        'school.subject.line', 'student_id', string='Subject Lines')
    name = fields.Char(string='Name', required=True)
    mobile_no = fields.Char(string='Mobile No.')
    email_id = fields.Char(string='Email', required=True)
    address = fields.Text(string='Address', required=True)
    active = fields.Boolean(default=True)

    student_cnt = fields.Integer('Students', compute='get_student_cnt')
    # unique constraints
    _sql_constraints = [
        ('emailid_uniq', 'unique(email_id)',
         'Email must be unique!'),
        ('mobileno_uniq', 'unique(mobile_no)',
         'Mobile No. must be unique!'),
    ]

    # @api.constrains("email_id")
    # def check_email_id(self):
    #     for rec in self:
    #         search_rec = self.env['school.professor.detail'].search(
    #             [('email_id', '=', str(rec.email_id))])
    #         if search_rec.id:
    #             raise ValidationError("Email id already exist.")

    def get_student_cnt(self):
        st_cnt = self.env['school.student.detail'].search_count([])
        self.student_cnt = int(st_cnt)

    @api.constrains("mobile_no")
    def check_mobile_no(self):
        if str(self.mobile_no).strip() != 'False':
            print("\n\n\n True \n\n\n")
            if not str(self.mobile_no).isdigit():
                raise ValidationError("Please enter valid mobile no.")
            else:
                if len(str(self.mobile_no).strip()) != 10:
                    raise ValidationError("mobile no. size must be 10.")

    # @api.constrains("email_id")
    # def check_email_id(self):
    #     if str(self.email_id).strip() != 'False':
    #         print("\n\n\n True \n\n\n")
    #         if (str(self.email_id).strip()).find("@") != -1:
    #             raise ValidationError("email ID must be contains @.")

    # @api.model
    # def create(self, vals):
    #     print(f"\n\n\n professor input dt : {vals}\n\n\n")
    #     professor_obj = super(Professors, self).create({
    #         'name': vals['name'],
    #         'email_id': vals['email_id'],
    #         'address': vals['address'],
    #         'subject_line_ids': [(0, 0, {
    #             'sub_name': 'physcis',
    #             'sub_desc': 'desc of sub'
    #         })]

    #     })
    #     print(f"\n\n\n professor input dt : {vals}\n\n\n")
    #     return professor_obj

    # def write(self, vals):
    #     vals['email_id'] = 'aktiv_new@gmail.com'
    #     # professor_obj = super(Professors, self).search([])
    #     proofessor_write_q = super(Professors, self).write({
    #         'email_id': vals['email_id'],
    #         'subject_line_ids': [(0, 0, {
    #             'sub_name': 'maths',
    #             'sub_desc': 'desc of maths'
    #         })]
    #     })
    #     print(f"n\n\n{type(proofessor_write_q)}\n\n\n")
    #     return proofessor_write_q

    # def write(self, vals):
    #     print(f"\n\n\n{super(Professors, self).read()}\n\n\n")
    # professors_records = super(Professors, self).read(['subject_line_ids'])
    #     print(f"\n\n\n\n{professors_records[0]['subject_line_ids']}\n\n\n\n")

    #     subject_lines_ids = professors_records[0]['subject_line_ids']
    #     single_sub_id = subject_lines_ids[0]['subject_line_ids'][0]

    #     return self.env["school.subject.line"].browse(
    #         [single_sub_id]).write({
    #             'sub_name': 'master',
    #             'sub_desc': 'fthuutyu'
    #         })

    def action_student(self):

        # self.ensure_one()

        return {
            'type': 'ir.actions.act_window',
            'name': 'Students tree view',
            'view_mode': 'tree',
            'res_model': 'school.student.detail',
        }
