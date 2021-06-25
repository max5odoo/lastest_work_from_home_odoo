from datetime import time

from odoo import api, fields, models
from random import randint


class Students(models.Model):
    _inherit = 'student.student'
    tasks_name = fields.One2many('tasks.tasks', 'student_id', string='Task names')


class Professor(models.Model):
    _inherit = 'professor.professor'


class task(models.Model):
    _name = 'tasks.tasks'
    _description = 'task description'
    _rec_name = 'task_name'

    def _get_default_color(self):
        return randint(1, 11)

    student_id = fields.Many2one('student.student', string='Student')
    task_name = fields.Char(string='Task Name')
    task_technology = fields.Char(string='Task Technology Used')
    professor_id = fields.Many2one('professor.professor', string='many2one vadi')
    professor_name_many2one = fields.Char(related='professor_id.address', string='professor name')
    task_done = fields.Boolean()
    task_not_done = fields.Boolean()
    task_start_time = fields.Datetime(string='Task Start Date', required=False)
    task_end_time = fields.Datetime(string='Task end Date', required=False
                                    )
    company_name = fields.Char("Company Name", placeholder="enter the comapny name")
    color = fields.Integer(string='Color Index', default=_get_default_color)

