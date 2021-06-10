import random
from string import digits

from odoo import models, fields, api


class Course(models.Model):
    _name = "course.details"
    _description = "Course details"
    _rec_name = "course_name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    course_name = fields.Char(string="Course Name")
    no_of_years = fields.Integer(string="No of Years", required=True)
    student_ids = fields.One2many('student.details', 'course_id', string="Students")
    # mobile_no = fields.Integer(string="Mobile no.")
    # email = fields.Char(related='student_ids.email',string="Email")
    # s_id = fields.Integer(related='student_ids.roll_no', string="Roll no.")
    no_of_students = fields.Integer(compute='count_students', string="No of Students",
                                    readonly=True, store=True)
    batch_id = fields.One2many('batch.details', 'course_ids', string="Batch")
    currency_id = fields.Many2one('res.currency', string="Currency", readonly=True,
                                  default=lambda self: self.env['res.currency'].browse([20]),
                                  invisible=True)
    fees = fields.Monetary(string="Fees")
    sequence = fields.Integer(string="seq")
    color = fields.Integer('color_field')

    @api.depends('student_ids')
    def count_students(self):
        count = 0
        for rec in self:
            for j in rec.student_ids:
                count += 1
                rec.no_of_students = count

    def name_get(self):
        res = []
        for course in self:
            res.append((course.id, course.course_name + '-' + str(course.no_of_years)))
        return res

    @api.model
    def default_get(self, fields_list):
        res = super(Course, self).default_get(fields_list)
        res['course_name'] = 'Course 1'
        res['no_of_years'] = '3'
        return res

    # def write(self,vals):
    # 	return super(Course, self).write(vals)

    # @api.model
    # def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=1):
    # 	if args is None:
    # 		args=[]
    # 	domain = args + ['|',('roll_no',operator,name),('student_ids',operator,name)]
    # 	return super(Course, self)._name_search(domain, limit=limit).name_get()

    def test(self):
        for i in range(2):
            course_name = 'Course by cron' + ''.join(random.choice(digits) for i in range(1))
            no_of_years = ''.join(random.choice(digits) for i in range(1))
            name = 'Shivam by cron' + ''.join(random.choice(digits) for i in range(1))
            name2 = 'Shivam by cron' + ''.join(random.choice(digits) for i in range(1))
            vals = {
                'course_name': course_name,
                'no_of_years': no_of_years,
                'student_ids': [(0, 0, {
                    'name': name,
                    'student_email': 'shivam@cron.com',
                    'mobile_no': '6363636363',
                    'roll_no': 333,
                    'age': 21
                }),
                                (0, 0, {
                                    'name': name2,
                                    'student_email': 'shivam@cron.com',
                                    'mobile_no': '6363636363',
                                    'roll_no': 333,
                                    'age': 23
                                })]
            }
            print(f"\n\n\n---{vals}==\n\n\n")
            self.create(vals)

    def _multi_write(self):
        c_ids = self.env['course.details'].browse([(1)])
        for rec in c_ids:
            course_name = 'Course by cron' + ''.join(random.choice(digits) for i in range(1))
            no_of_years = ''.join(random.choice(digits) for i in range(1))

            vals = {
                'course_name': course_name,
                'no_of_years': no_of_years,
                'student_ids': [(0, 0, {
                    'name': 'Shivam by cron',
                    'student_email': 'shivam@cron.com',
                    'mobile_no': '6363636363',
                    'roll_no': 333,
                    'age': 23
                })]
            }
            print(f"\n\n\n---{vals}==\n\n\n")
            rec.write(vals)

    def delete_course(self):
        # for rec in self:
        # Unlink all the records using (5,0,0) and create and link static
        # rec.student_ids = [(5,0,0),
        # 				   (0,0,{
        # 					'name' : [(4,9)],
        # 					'roll_no': 12,
        # 					'age': 19,
        #
        # })]
        # student record using (0,0,values)

        # a = self.env['student.details'].create(
        # 	{
        #
        # 		'name': [(4, 22)],
        # 		# 'email': 'shivam@cron.com',
        # 		# 'mobile_no': '6363636363',
        # 		'roll_no': 333,
        # 		'age': 23
        # 	}
        # )
        # #
        # rec.student_ids = [(4,a.id)]
        # rec.student_ids = [(4,1)]

        # Unlink and link the student records having ids(1,2)
        # rec.student_ids = [(6,0,[1,2])]

        # Update the student record's(id=1) name attribute using (1,id,values(dict))
        # rec.student_ids = [(1,1,{'name':'thaygayu'})]  #----------> Here (1,id,{values}) format is followed

        # Unlink from the field and delete the record from database as well
        # rec.student_ids = [(2,13)] #----------> Here (2,id) format is followed

        # unlink the specific record having id = 1 it will not delete the record from student
        # rec.student_ids = [(3,1)]

        # def create_user(self):
        # vals = {
        # 	'name': 'python 4',
        # 	'login': 'Python4',
        # 	'password': '1234',
        # 	'sel_groups_1_9_10': '1',
        # 	'sel_groups_44_45': '45',
        # }
        # res = self.env['res.users'].create(vals)
        # print(f"\n\n---{res}--\n\n")

        pass

    def go_to_batch(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'batch.details',
            'view_mode': 'tree,form',
        }

    def go_to_student(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'student.details',
            'view_mode': 'tree,form',
            'domain': [('course_id', '=', self.ids)]
        }
