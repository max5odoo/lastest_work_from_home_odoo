from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError,AccessError

class Batch(models.Model):
	_name = "batch.details"
	_description = "batch details"
	_rec_name = "batch_name"

	batch_name = fields.Char(string="Batch Name")
	total_seats = fields.Integer(string="Total seats",required=True)
	course_ids = fields.Many2many('course.details','batch_course_rel','batch_id',
							  'course_id',string="Course")
	remaining_seat = fields.Integer(string="Remaining seats", compute="count_remaining_seat" ,readonly=True, store=True)
	date_field = fields.Date(string="Date")
	currency_id = fields.Many2one(related='course_ids.currency_id', string="Currency", readonly=True,
								  default=lambda self: self.env['res.currency'].browse([20]))
	total_fees = fields.Monetary(string="Total Fees", compute="find_fees", readonly=True, store=True)

	@api.depends('course_ids')
	def find_fees(self):
		course = self.course_ids.ids
		t_fee = self.env['course.details'].search([('id', 'in', course)])
		total = sum(t_fee.mapped('fees'))
		self.write({
			'total_fees':  total,
		})

	@api.model
	def create(self, vals):
		vals['date_field'] = date.today()
		print(f"\n\n\n--------------{vals}----------\n\n\n")
		# if (vals.get('total_seats') <= 10):
		# 	raise ValidationError("Seats can't be less than 8.")
		res = super(Batch, self).create(vals)
		return res

	@api.depends('course_ids')
	def count_remaining_seat(self):

		#METHOD 2

		for rec in self:
			courses = rec.course_ids.ids    #get the ids of the courses

			#keep the courses
			records = rec.env['course.details'].search([('id','in',courses)])

			#add the numbers when we choose a course
			seats = sum(records.mapped('no_of_students'))
			rec.write(
						{
							'remaining_seat': rec.total_seats - seats,
						}
					)

		# METHOD1

		# for rec in self:
		# 	courses = rec.course_ids.ids
		# 	seats = 0
		# 	for course in courses:
		# 		seats+=rec.env['course.details'].browse(course).no_of_students
		#
		# 	rec.write(
		# 				{
		# 					'remaining_seat' : rec.total_seats - seats,
		# 				}
		# 			)

			# print(f"\n\n\n------course_ids-------{rec.course_ids.ids}---------\n\n\n")
			# count_s = 0
			# print(f"\n\n\n------course_ids-------{rec.course.ids}---------\n\n\n")
			# course_ids = rec.course.ids
			# count_s=self.env['course.details'].browse(course_ids).no_of_students
			
			# self.write({
   #         		'remaining_seat': rec.total_seats - count_s
   #          })

	# def read(self, fields, load='_classic_read'):
	# 	if self.check_access_rights('read', raise_exception=False):
	# 		return super(Batch, self).read(fields, load=load)
	# 	private_fields = set(fields).difference(self.env['batch.details']._fields.keys())
	# 	if private_fields:
	# 		raise AccessError('The fields "%s" you try to read is not available on the Batch profile.' % (
	# 			','.join(private_fields)))
	# 	return self.env['batch.details'].browse(self.ids).read(fields, load=load)
