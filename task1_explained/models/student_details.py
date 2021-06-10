from odoo import models, fields, api, _, modules
from datetime import date
from odoo.exceptions import ValidationError, UserError, AccessError
from odoo.modules.module import get_resource_path
import base64
import requests
from lxml import etree
import random
from string import ascii_lowercase,ascii_letters,ascii_uppercase, digits


import re


class ContactInherite(models.Model):
	_inherit = "res.partner"
	# _order = 'id desc'
	is_student = fields.Selection([('student', 'Student'), ('professor', 'Professor')],
											string='Student Or Professor', required=True, default='student',
											help="Select any one student or professor")



class Student(models.Model):
	_name = "student.details"
	_description = "Student"
	_rec_name = 'name'
	_inherit = 'abstract.for.age'

	# @api.model
	# def _get_default_image(self):
	# 	with open(modules.get_module_resource('school', 'static/description', 'user.png'), 'rb') as img:
	# 		image = base64.b64encode(img.read())
	# 	return image

	partner_id = fields.Many2one('res.partner', "PRO")
	name = fields.Many2one('res.partner', string="Student")
	photo = fields.Image(related="name.image_1920", string="Photo")
	unique_name = fields.Char(string='Sr. No', readonly=True, required=True, copy=False, index=True, default=lambda self: _('New'))
	mobile_no = fields.Char(related='name.phone', string="Mobile no.")
	student_email = fields.Char(related='name.email', string="Email.")
	course_id = fields.Many2one('course.details', string='Courses')
	# dob = fields.Date(string="Date Of Birth")
	# age = fields.Integer(string="Age",compute='compute_age',store=True,readonly= True)
	his_professor = fields.Many2one('professor.details', string="Professor", readonly=True)

	#DOMAIN DECLARATION IN FIELDS
	# s_id = fields.Many2one('course.details',string='S_id',domain=[('s_id','!=','course 1')])
	# student_batch = fields.One2many('batch.detais', 'student_in_batch',String = "Batch")

	roll_no = fields.Integer(string="Roll no.")
	sequence = fields.Integer(string=".")
	gender = fields.Selection([
		('male','Male'),
		('female','Female')
	], default="male", string='Gender')
	total_registrations = fields.Integer(string="Registrations", compute="total_registrations_")
	skill_type_id = fields.One2many('student.skill', 'name', string='Skill')
	active = fields.Boolean(default=True)

	@api.model
	def create(self, vals):
		if vals.get('unique_name', 'New') == 'New':
			vals['unique_name'] = self.env['ir.sequence'].next_by_code(
				'student.details') or 'New'

		result = super(Student, self).create(vals)
		return result


	# def create(self, vals):
	# 	# data = base64.b64encode(self.photo)
	# 	vals['photo'] = base64.b64encode(vals.get('photo'))
	# 	res = super(Student, self).create(vals)
	# 	return res


	def name_get(self):
		res = []
		for student in self:
			name = f"{student.name.name}-{student.roll_no}"
			if self.env.context.get("csk"):
				name = f"{student.name.name}"
			res.append((student.id, name))
		return res
		return res

	def total_registrations_(self):
		count = self.env['registrations.details'].search_count([('student', '=', self.id)])
		self.total_registrations = count

	# _sql_constraints = [
	# ('email_uniq', 'unique (email)', 'Email is  already taken !')
	# ]


	# @api.depends('dob')
	# def compute_age(self):
	# 	today = date.today()
	# 	for rec in self:
	# 		if rec.dob:
	# 			# print(f"\n\n\n----dob value-------{rec.dob}------dob type-------{type(rec.dob)}-----\n\n\n")
	# 			rec.age = abs((today-rec.dob).days//365)

	# @api.constrains('age')
	# def check_age(self):
	# 	for rec in self:
	# 		if rec.age < 18:
	# 			raise ValidationError("Age must be at least 18")

	#-------------------THE SAME THING CAN BE DONE USING ORM METHOD SEARCH BY JUST GIVING
	#----------DOMAIN IN METHID LIKE---->  self.env['student.details'].search([('age','>=',18)])
	# @api.constrains('email')
	# def check_email(self):
	# 	for rec in self:
	# 		result = rec.env['student.details'].search([('email','=',rec.email)])
	# 		if result.id:
	# 			raise ValidationError("Email already exists")

	@api.constrains('mobile_no')
	def check_mobileno(self):
		for rec in self:
			if rec.mobile_no:
				a = len(rec.mobile_no)
				if a < 10 or a > 10:
					raise ValidationError("Mobile number must have 10 digits.")

	# def write(self, vals):
	# 	print(f"--------vals------{vals}")
	# 	for rec in self:
	# 		if 'dob' in vals:
	# 			if rec.dob != vals.get('dob'):
	# 				raise UserError('You can not change the DOB.')
	#
	# 	a = self.env['student.details'].search([('name','=','Shivam')])
	# 	print(f"\n\n\n\n-----------B--------{a}---------\n\n\n\n")
	# 	res = super(Student, self).write(vals)
	# 	return res

	@api.model
	def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=1):
		if args is None:
			args = []
		domain = args + ['|',('roll_no',operator,name),('name',operator,name)]
		# return super(Student, self)._name_search(domain, limit=limit).name_get()
		return self._search(domain, limit=limit, access_rights_uid=name_get_uid)


	# def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
	#
	# 	res = super(Student, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
	#
	# 	#it will generate a dynamic field in the place of 'age'
	#
	#
	# 	""" this is for view type = form """
	# 	if view_type=='form':
	# 		doc = etree.XML(res['arch'])
	# 		dynamic_field = doc.xpath("//field[@name='age']")
	# 		if dynamic_field:
	# 			dynamic_field[0].addnext(etree.Element('label', {'string': 'Hello ,,This is a dynamically created field..'}))
	# 			res['arch'] = etree.tostring(doc, encoding='unicode')
	# 	# to set value of create lable we can simply write :
	# 	#
	# 	# 		dynamic_fields.set('string','dlkshrgvj')
	#
	# 	""" this is for view type = tree """
	#
	# 	if view_type=='tree':
	# 		doc = etree.XML(res['arch'])
	# 		new_field = doc.xpath("\\field[@name='roll no']")
	# 		if new_field:
	# 			new_field[0].addnext(etree.Element('field',{'string' : 'Rollll', 'name': 'rollll'}))
	# 		res['arch'] = etree.tostring(doc, encoding='unicode')
	# 	return res

	# create method for cron
	# 	def test(self):
	# 		for i in range(1):
	# 			name = ''.join(random.choice(ascii_uppercase) for i in range(1)) + ''.join(
	# 				random.choice(ascii_lowercase) for i in range(4))
	# 			mobile_no = ''.join(random.choice(digits) for i in range(10))
	# 			age = ''.join(random.choice(digits) for i in range(2))
	# 			check = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17']
	# 			roll_no = i+100
	#
	# 			if age not in check:
	# 				vals_list = {'name': name, 'mobile_no': mobile_no, 'age': age, 'gender': 'female', 'roll_no': roll_no}
	# 				vals_list['course_id'] = 1
	# 				print(f"\n\n---{vals_list}--\n\n\n")
	# 				self.create(vals_list)

	# this method is for open wizard through button object
	def wiz_open(self):
		return {
			'type': 'ir.actions.act_window',
			'res_model': 'registration.wizard',
			'view_mode': 'form',
			'target': 'new',
			'context': {'default_student_id': self.id}
		}

	def go_to_regi(self):
		result = self.env['registrations.details'].search([('student', 'in', self.ids)])
		print(f"\n\n\n--->>>{result.student.name.name}<<<---\n\n\n")
		print(f"\n\n\n--->>>{self.id}<<<---\n\n\n")

		if result:
			return {
				'type': 'ir.actions.act_window',
				'res_model': 'registrations.details',
				'domain': [('student', 'in', self.ids)],
				'view_mode': 'tree,form',
				'target': 'current',
				'context': {
					'search_default': self.name.id,
				}
			}
		else:
			return {
				'type': 'ir.actions.act_window',
				'res_model': 'registrations.details',
				'view_mode': 'form',
				'context': {
					'default_student': self.id,
				}
			}


	def go_to_course(self):
		result = self.env['course.details'].search([('course_name', '=', self.course_id.course_name)])
		if result:
			return {
				'type': 'ir.actions.act_window',
				'res_model': 'course.details',
				'view_mode': 'tree,form',
				'domain': [('course_name', '=', self.course_id.course_name)],
				'context': {'search_default_course_name': self.course_id.course_name},
			}
		else:
			raise AccessError("You haven't selected any course yet.")

	def go_to_batch(self):
		return {
			'type': 'ir.actions.act_window',
			'res_model': 'batch.details',
			'view_mode': 'tree,from',
		}

	# method for report
	def get_report(self):
		return self.env.ref('task1_explained.student_report').report_action(self)

	def send_email(self):
		template_id = self.env.ref('task1_explained.student_email').id
		compose_form_id = self.env.ref('mail.email_compose_message_wizard_form').id
		self.ensure_one()
		# ir_model_data = self.env['ir.model.data']
		# try:
		# 	template_id = ir_model_data.get_object_reference('task1_explained',   'student_email')[1]
		# except ValueError:
		# 	template_id = False
		# try:
		# 	compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
		# except ValueError:
		# 	compose_form_id = False

		reg = self.env['registrations.details'].search([("student","=",self.id)])
		reg_url = f"/web#id={str(reg.id)}&view_type=form&model=registrations.details"
		ctx = {
			'default_model': 'student.details',
			'default_res_id': self.ids[0],
			'default_use_template': bool(template_id),
			'default_template_id': template_id,
			'default_composition_mode': 'comment',
			'mark_so_as_sent': True,
			'force_email': True,
			'reg_url': reg_url,
		}
		return {
			'type': 'ir.actions.act_window',
			'view_type': 'form',
			'view_mode': 'form',
			'res_model': 'mail.compose.message',
			'views': [(compose_form_id, 'form')],
			'view_id': compose_form_id,
			'target': 'new',
			'context': ctx,
		}
