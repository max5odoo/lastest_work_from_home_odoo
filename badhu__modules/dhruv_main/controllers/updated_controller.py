from odoo import http, _
from odoo.http import request
from odoo.tools import groupby as groupbyelem
from operator import itemgetter
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager

from odoo.osv.expression import OR
import base64
import json


class StudentNewDetail(http.Controller):
	@http.route('/studentpage', type='http', auth='public', website=True) #table page render
	def studentpage(self):
		return http.request.render('dhruv_main.student_table_page')



	@http.route('/studentdata', type='http',auth="public",cors="*",website=True) #for table data 
	def studentdata(self):
		student_recs = request.env["school.student.detail"].search([])
		print(student_recs)

		
		students = []

		for student in student_recs:
			vals = {
				'id' : student.id,
				'name' : student.name,
				'avatar_img' : student.avatar_img,
				'gender' : student.gender,
				'email_id' : student.email_id,
				'address_line1' : student.address_line1

			}
			students.append(vals)

		data = {
			'students' : students 
		}	

		print(type({"msg" : 'this is msg'}))
		print(type(json.dumps({"msg" : 'this is msg'})))
		# return json.dumps({'msg' : 'this is msg'})
		return json.dumps(data)

			


