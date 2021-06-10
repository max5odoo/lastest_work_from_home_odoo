from odoo import api,models,fields

class RegistrationShowWizard(models.TransientModel):
    _name = 'registration.wizard'
    _description = 'Wizard'

    student_id = fields.Many2one('student.details', string="Student", required=True)

    def go_to_regi(self):
        print(f"\n\n--Goto Regi--\n\n")
        print("\n\n\n self._context",self._context)
        result = self.env['registrations.details'].search([('student','=',self.student_id.id)])
        print(f"\n\n----result---{result}--\n\n")
        print(f"\n\n----student_id---{self.student_id.id}--\n\n")
        if result:
            return {
                        'type': 'ir.actions.act_window',
                        'res_model': 'registrations.details',
                        'domain': [('student', '=', self.student_id.id)],
                        'view_mode': 'tree,form',
                    }
        else:
            return {
                        'type': 'ir.actions.act_window',
                        'res_model': 'registrations.details',
                        # 'domain' : [('student','=',self.student_id.id)],
                        'view_mode': 'form',
                        'context': {
                            'default_student': self.student_id.id,
                        }
                    }

