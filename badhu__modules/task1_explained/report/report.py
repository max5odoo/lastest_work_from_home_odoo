from odoo import models, api


class ProfessorInReport(models.AbstractModel):
    _name = 'report.task1_explained.student_report_t1'
    _description = 'report.task1_explained.student_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        # print(f"\n{docids}\n{data}\n{self.env.context}\n{self}")
        model = self.env.context.get('active_model')
        docs = self.env['student.details'].browse(docids[0])
        professor = self.env['professor.details'].search([('his_students', '=', docids[0])])
        batch = self.env['batch.details'].search([])
        # print(f"\nbatch---{batch}\n")
        batch_list = []
        p_list = []

        for rec in batch:
            b_vals = {
                'batch_name': rec.batch_name,
                'total_seats': rec.total_seats,
                'total_fees': rec.total_fees,
                'course_ids': [i.course_name for i in rec.course_ids],
            }
            # print(f"\n{[i.course_name for i in rec.course_ids]}\n")
            # print(f"\n{b_vals}\n")
            batch_list.append(b_vals)
        print(f"batch----{b_vals}")
        for rec in professor:
            vals = {
                'professor_name': rec.professor_name.name,
                'mobile_no': rec.mobile_no,
                'email': rec.email,
            }
            p_list.append(vals)
        # print(f"\n\nprofessor----{p_list}")

        return{
            'doc_model': 'student.details',
            'docs': docs,
            'data': data,
            'p_list': p_list,
            'batch_list': batch_list,
        }
