from odoo.tests import common


class Teststudent(common.TransactionCase):
    def setUp(self):
        super(Teststudent, self).setUp()

        self.student = self.env['student.student']
        # create an student record
        self.student1 = self.student.create({
            'name': 'student',
            'address': 'Ahmedabad, india',
            'student_email': 'student1@gmail.com',
            'phoneno': 9898989898,


        })

    def test_compute_student_data(self):
        '''
      This function test the student function functionality
      Here name of student
      '''

        # check name of the student1
        self.assertEqual(self.student1.name, 'rthrty')


