from odoo import fields, api, models


class Manthan(models.Model):
    _name = "manthan.manthan"
    _description = "manthan.manthan"

    name = fields.Char('Manthan')
    no = fields.Integer('no')

    def name_get(self):
        res = []
        for manthan in self:
            name = f"{manthan.name}-{manthan.no}"
            if self.env.context.get("www"):
                name = f"{manthan.name}"
            res.append((manthan.id,name))
        return res

    def copy(self, default={}):
        self.ensure_one()
        print(f"\n\n\nSELF--->>>{self.name}<<<---\n\n\n")
        print(f"\n\n\nDEFAULT--->>>{default}<<<---\n\n\n")
        default['name'] = self.name + "(copy)"
        default['no'] = 251298
        return super(Manthan, self).copy(default=default)

    @api.model
    def name_create(self, name):
        print(f"\n\n\n--->>>{name}<<<---\n\n\n")
        return super(Manthan, self).name_create(name)

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=1):
        if args is None:
            args = []
        domain = args + ['|', ('no', operator, name), ('name', operator, name)]
        return self._search(domain, limit=limit, access_rights_uid=name_get_uid)