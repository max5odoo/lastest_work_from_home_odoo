# -*- coding: utf-8 -*-
from openerp import models, fields, api

# Non-odoo library
import random
from random import randint
import string


class button_action_demo(models.Model):
    _name = 'button.demo'

    user_name = fields.Char(required=True, default='Click on generate name!')
    password = fields.Char()
    name = fields.Char('name')
    password_search = fields.Char('pasword search karelo')

    def generate_record_name(self):
        self.ensure_one()
        # Generates a random name between 9 and 15 characters long and writes it to the record.
        self.user_name = ''.join(
            random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(9, 15)))

    def search_func(self):
        # search_res = self.env['button.demo'].search(
        #      [('name', '=', 'manthan')])
        # print(f"\n\n\n search() res : {search_res} \n\n\n")
        # # search_count
        # search_cnt = self.env['student.student'].search_count(
        #     ['', ])
        # search_read = self.env['button.demo'].search_read([('name', '=', 'manthan')], fields=['password'])
        # self.password_search=search_read[0].get('password')
        # print(f"\n\n\nsearch_read {search_read}\n\n\n")
        read_first = self.env['student.student'].search([('name','=','manthan')]).read(['gender'])
        print(f'\n\n\n\n\ntype({read_first}) this return list of dictionary\n\n\n\n')
        # self.password_search=str(read_first[2].get('password'))
        print(f"\n\n\nsearch_read {read_first}\n\n\n")
