from odoo import api, models, fields


class StudentFeesWizard(models.TransientModel):
    _name = "school.student.fees.wizard"

    def set_data(self):
        fees = self.env['school.student.detail'].browse(
            self._context.get("active_id")).read(['fees'])
        print(f"n\n\n {fees} \n\n\n")
        new_fees = fees[0]['fees']
        return new_fees

    fees = fields.Float(default=set_data)

    def update_student_fees(self):
        print(f"\n\n\n fees updated successfully...  \n\n\n")
        print(self.env['school.student.detail'].browse(
            self._context.get("active_id")))
        self.env['school.student.detail'].browse(
            self._context.get("active_id")).write({'fees': self.fees})
        return True
