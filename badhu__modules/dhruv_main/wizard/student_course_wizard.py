from odoo import api, models, fields


class StudentCoursesWizard(models.TransientModel):
    _name = "school.student.courses.wizard"

    course_ids = fields.One2many(
        'school.student.courses.wizard.line', 'w_id', string='Course Lines')
    course_line_ids = fields.Many2many(
        'courses.detail', 'student_course_rel_wizard', 'student_course_wiz_id', 'course_id', string='Courses')
    #

    def update_courses(self):
        print("\n\n\n courses updated by wizard \n\n\n")
        # self.course_line_ids.course_id
        print(f"\n\n\n {self.course_line_ids.ids} \n\n\n")

        courses_list_ids = self.course_line_ids.ids

        # courses = []
        # for i in range(len(courses_list_ids)):
        #     dt = self.env['courses.detail'].browse(courses_list_ids[i])
        #     print(f"\n\n\n {dt} \n\n\n")
        #     courses.append(dt)

        for i in range(len(courses_list_ids)):
            print(f"\n\n\n {courses_list_ids[i]} \n\n\n")
            # link  id to student one2many fields
            self.env['school.student.detail'].browse(self._context.get("active_id")).write({
                'course_ids': [
                    (0, 0, {
                        'course_id': courses_list_ids[i]
                    })
                ]
            })

        return True
    # def update_courses(self):
    #     print("\n\n\n courses updated by wizard \n\n\n")

    #     # get list of courses which added by user
    #     # print(f"\n\n {self.course_ids.ids} \n\n")
    #     # print(f"\n\n\n {self.browse([self.course_ids.ids[0].id])}")
    #     c_ids = self.env["school.student.courses.wizard.line"].search(
    #         [('w_id', '=', self.id)])
    #     print(f"\n\n\n {c_ids.course_id}, {c_ids.course_id.ids}")

    #     # get ids from that one2many field
    #     # loop for ids
    #     f_ids = []
    #     for i in range(len(c_ids.course_id.ids)):
    #         # self.env['school.student.detail'].browse(self._context.get("active_id")).write({
    #         #     'course_ids': [
    #         #         (4, c_ids.course_id[i])
    #         #     ]
    #         # })
    #         f_ids.append(self.env['course.data.lines'].search(
    #             [('course_id', '=', c_ids.course_id.ids[i])], limit=1))

    #     print(f"\n\n\n {f_ids}")

    #     for i in range(len(f_ids)):
    #         # link that id to student one2many fields
    #         self.env['school.student.detail'].browse(self._context.get("active_id")).write({
    #             'course_ids': [
    #                 (4, f_ids[i].id)
    #             ]
    #         })


class StudentCoursesWizardLine(models.TransientModel):  # task.lines
    _name = 'school.student.courses.wizard.line'

    course_id = fields.Many2one('courses.detail', ondelete="set default")
    short_desc = fields.Char(string="Short Desc.",
                             related='course_id.short_desc')
    created_by = fields.Char(
        string="Created By", related='course_id.created_by')
    w_id = fields.Many2one('school.student.courses.wizard')

    def name_get(self):
        label = []
        for rec in self:
            title = f"{rec.course_id.name} ({rec.st_id.name})"
            label.append((rec.id, title))
        return label
