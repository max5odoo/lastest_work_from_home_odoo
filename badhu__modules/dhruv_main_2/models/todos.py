from odoo import api, fields, models


class Todos(models.Model):
    _name = "todos.detail"
    _description = "todos detail"
    _rec_name = "title"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    is_done = fields.Boolean(string="Is Completed", default=False)
    start_datetime = fields.Datetime()
    end_datetime = fields.Datetime(string="End DateTime")

    def name_get(self):
        label = []
        for rec in self:
            title = f"{rec.title} ({rec.is_done})"
            label.append((rec.id, title))
        return label

    # def name_get(self):
    #     professor_context = self.env.context.get("todo_context")
    #     label = []
    #     if professor_context:
    #         # keep as it is
    #         for rec in self:
    #             title = f"{rec.title}"
    #             label.append((rec.id, title))
    #     else:
    #         # combine 3 fields
    #         for rec in self:
    #             title = f"({rec.id}) - {rec.title} ({rec.is_done})"
    #             label.append((rec.id, title))
    #     return label
