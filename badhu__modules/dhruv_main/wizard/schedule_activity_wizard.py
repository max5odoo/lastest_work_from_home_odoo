from odoo import api, models, fields


class ScheduleActivityWizard(models.TransientModel):
    _name = "schedule.activity.wizard"

    def set_activity_type(self):
        data = self.env['mail.activity.type'].search([('name', '=', 'To Do')])
        return data

    activity_type = fields.Many2one(
        'mail.activity.type', default=set_activity_type)
    due_date = fields.Date()
    assign_to = fields.Many2one(
        'res.users', default=lambda self: self.env.user)
    summary = fields.Char()
    note = fields.Text()

    def add_new_activity(self):
        print(f"\n\n\n new activity added successfully \n\n\n")

        res_model = self.env['ir.model'].search(
            [('model', '=', self.env.context.get('active_model'))])
        print(f"\n\n\n {res_model.model} \n\n\n")
        new_activity = self.env["mail.activity"].create({
            'res_model_id': res_model.id,
            'res_id': self.env.context.get('active_id'),
            'activity_type_id': self.activity_type.id,
            'date_deadline': self.due_date,
            'summary': self.summary

        })

        return new_activity
