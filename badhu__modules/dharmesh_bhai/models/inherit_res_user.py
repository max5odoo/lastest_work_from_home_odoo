from odoo import models, fields, api


class InheritResuser(models.Model):
    _inherit = "res.users"

    @api.model
    def create(self, vals):
        vals['groups_id'] = [(4, self.env.ref('student_app.proffessor').id)]
        rtn = super(InheritResuser, self).create(vals)
        return rtn

