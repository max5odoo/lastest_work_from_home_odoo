from odoo import fields, api, models


class Shivam(models.Model):
    _name = "shivam.shivam"
    _description = "shivam.shivam"

    name = fields.Many2one('manthan.manthan')
    no = fields.Integer('no', default=100)

    def copy(self, default={}):
        self.ensure_one()
        print(f"\n\n\nSELF--->>>{self.name.id}<<<---\n\n\n")
        print(f"\n\n\nDEFAULT--->>>{default}<<<---\n\n\n")
        default['no'] = 2525
        return super(Shivam, self).copy(default=default)

    # @api.model
    # def default_get(self, fields_list=[]):
    #     print(f"\n\n\n--->>><<<---\n\n\n")
    #     print(f"\n\n\n--->>>{fields_list}<<<---\n\n\n")
    #     res = super(Shivam, self).default_get(fields_list)
    #     print(f"\n\n\n--->>>{res}<<<---\n\n\n")
    #     return res


    # @api.model
    # def create(self, vals_list):
    #     hh = self.env['shivam.shivam'].default_get(['no'])
    #     print(f"\n\n\n--->>>{hh}<<<---\n\n\n")
    #     result = super(Shivam, self).create(vals_list)
    #     return result
