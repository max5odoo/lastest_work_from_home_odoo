import base64
from urllib import response

from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo import http, _
from odoo.http import request
from odoo.exceptions import AccessError, MissingError
from odoo.http import request, route
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.tools import groupby as groupbyelem
from operator import itemgetter


class Homepage_student(http.Controller):
    @http.route(['/home', '/home/page/<int:page>'], type='http', auth='public', website=True)
    def student_details(self, page=1, sortby=None, groupby=None, **kw):
        # <-----------------NICHE VADO CODE is used to get the ALL STUDENT  data ----->
        # students_details = request.env['student.student'].sudo().search([])

        # <-----------------NICHE VADO CODE is used to get the current login user data ----->
        # request.env.user.id --->THIS IS USED TO GET THE WEBSITE USER ID
        values = {}
        searchbar_sortings = {
            'name': {'label': _('name'), 'order': 'name '},
        }

        searchbar_groupby = {
            'none': {'input': 'none', 'label': _('None')},
            'gender': {'input': 'gender', 'label': _('Gender')},

        }
        if not sortby:
            sortby = 'name'
        sort_order = searchbar_sortings[sortby]['order']

        # default group by value
        if not groupby:
            groupby = 'gender'

        domain = [('login_user', '=', request.env.user.id)]

        # task count
        task_count = request.env['student.student'].sudo().search_count(domain)
        print(f"\n\n\n\n\nthis is the task_counts {task_count}\n\n\n\n")

        # pager
        pager = portal_pager(
            url="/home",
            url_args={'sortby': sortby, 'groupby': groupby},
            total=task_count,
            page=page,
            step=3
        )

        students_details = request.env['student.student'].sudo().search(
            [('login_user', '=', request.env.user.id)], order=sort_order, limit=3, offset=pager['offset'])

        if groupby == 'gender':
            grouped_tasks = [request.env['student.student'].concat(*g) for k, g in
                             groupbyelem(students_details, itemgetter('gender'))]
            print(f"\n\n\n\n\nthis is the gender {grouped_tasks}\n\n\n\n")
        else:
            grouped_tasks = [students_details]

        values.update({
            'default_url': '/home',
            'grouped_tasks': grouped_tasks,
            'student_details': students_details,
            'sortby': sortby,
            'groupby': groupby,
            'searchbar_sortings': searchbar_sortings,
            'searchbar_groupby': searchbar_groupby,

            'pager': pager,
        })
        # print(f"\n\n\n\n this is student browse data{students_details}\n\n\n\n")
        return request.render('manthan.student_detail_page', values)

    # return http.Response(f'<h1 style="color:red;">hello manthan {data}</h1>') ----->>>> THIS IS WITH SIMPLE RESPONSE
    # '/home/<string:data>' ---->ane apde /home pachi lakhvanu for dynamic url thi page ma dekhay

    # this is the controller used for anchor tage for specific record

    @http.route(["/my/students/report/<int:student_id>"], type='http', auth='public', website=True)
    def student(self, student_id, report_type=None, access_token=None, download=False, **kw):
        student_rec = request.env['student.student'].browse([student_id])
        values = {}
        values.update({
            'students': student_rec
        })

        return request.render('manthan.student_report_onclick_', values)


# @http.route('/my/students/<int:student_id>', type='http', auth='public', website=True)
# def student(self, student_id, report_type=None, access_token=None, download=False, **kw):
#     student_rec = request.env['student.student'].browse([student_id])
#     try:
#         order_sudo = self._document_check_access('student.student', student_id, access_token=access_token)
#     except (AccessError, MissingError):
#         return request.redirect('/my/home')
#
#     if report_type in ('html', 'pdf', 'text'):
#         return self._show_report(model=order_sudo, report_type=report_type,
#                                  report_ref='manthan.report_student', download=download)
#     values = {}
#     values.update({
#         'students': student_rec
#     })
#     return request.render("manthan.student_my_task", values)


class Registration_student_route(http.Controller):
    @http.route('/register', type='http', auth='public', website=True)
    def student_registration(self):
        print("\n\n\n\n<--------successfully routeed----------->\n\n\n\n")
        return http.request.render('manthan.regi_form')


class Registration_student(http.Controller):
    @http.route('/create/student', type='http', auth='public', website=True)
    def student_registration(self, **kw):
        # BELOW CODE IS STUDENT REGISTRATION of NEW STYLE CODE
        if request.httprequest.method == 'POST':
            cnt = kw.get('count_no')
            print(f"\n\n\n this is the table count in python {cnt} \n\n\n")
            for i in range(0, int(cnt)):
                name = f'task_name{i + 1}'
                print(f"\n\n\n task_name:-- {i + 1} :  {kw.get(name)} \n\n\n")
                name = f'task_description{i + 1}'
                print(f"\n\n\n task_description:-- {i + 1} :  {kw.get(name)} \n\n\n")

            student_file = kw.get('student_profile').read()
            print(f'\n\n\n\n\n\n THIS IS THE STUDENT FILE UPLOADED{student_file}\n\n\n\n\n\n')
            values = {
                'name': kw.get('name'),
                'phoneno': kw.get('phoneno'),
                'gender': kw.get('gender'),
                'login_user': request.env.user.id,
                # BELOW IS USED FOR SUBMITTING THE FILE FROM WEBSITE
                'student_profile': base64.b64encode(student_file),

            }
            student_rec = request.env['student.student'].sudo().create(values)

            # --------------------------------THIS IS FOR THE ADDING ONE TO MANY FIELDS IN TABLE WEBSITE------------------------------------
            print(f'\n\n\n\nthis is the kw-->{kw}\n\n')
            for i in range(0, int(cnt)):
                new_task_name = f'task_name{i + 1}'
                task_name = kw.get(new_task_name)
                print(f'\n\n\n\nthis is the new task_name getting from table -->{task_name}\n\n\n\n')
                task_techno = f'task_description{i + 1}'
                task_technology = kw.get(task_techno)
                # +++++++++++++++++++++++ NICHE VADU 4,ID USE KARYU CHE ++++++++++++++++++++++++
                #         student_rec.write({
                #             'tasks_id': [(4, 1)]})
                # ++++++++++++++++++++++++++ 0,0 USE THAY CHE +++++++++++++++++++++++++
                student_rec.write({
                    'tasks_id': [(0, 0, {
                        'task_name': task_name,
                        'task_technology': task_technology
                    })]

                })
        # -------------------------------------------------------------------------------------------------------------
        return request.render('manthan.student_thanxs')

    # BELOW CODE IS STUDENT REGISTRATION OF OLDER CODE
    # students_registration = request.env['student.student'].sudo().create(kw)
    # print(f"\n\n\n\nthis is successfully registered--->>>{students_registration}\n\n\n\n")
    # return request.render('manthan.student_thanxs', {'student_details': students_registration})

    @http.route('/cancel', type='http', auth='public', website=True)
    def student_registration_cancle(self):
        print("\n\n\n\n<<<----------this is successfully Cancle--->>>\n\n\n\n")
        return request.redirect('/homepage')

    @http.route('/homepage', type='http', auth='public', website=True)
    def student_homepage(self):
        print("\n\n\n\n<<<----------this is successfully rendered Homepage  --->>>\n\n\n\n")
        student_name = request.env['student.student'].sudo().browse(request.session.uids)
        print(f"\n\n\n\nthis is successfully home session-->>>{student_name}\n\n\n\n")
        return request.render('manthan.homepage', {'student_name': student_name})

    @http.route('/signup', type='http', auth='public', website=True)
    def user_create(self, **kw):
        # print("\n\n\n\n<<<----------this is successfully rendered User page  --->>>\n\n\n\n")
        # user_details = request.env['res.users'].sudo().search([])
        # print(f"\n\n\n\nthis is successfully registered--->>>{user_details}\n\n\n\n")
        # # user_create = request.env['res.users'].sudo().create(kw)
        # # print(f"\n\n\n\nthis is successfully user created--->>>{user_create}\n\n\n\n")
        # if request.session.uid:
        #     pass
        # else:
        #     vals = {
        #         'name': 'manthan dhruv',
        #         'login': 'manthandhruv@gmail.com',
        #         'password': '12345',
        #         'sel_groups_1_9_10': '10',
        #     }
        #     user_create = request.env['res.users'].sudo().create(vals)
        #     print(f"\n\n\n\nthis is successfully user created--->>>{user_create}\n\n\n\n")
        if request.httprequest.method == 'POST':
            students_registration = request.env['student.student'].sudo().create(kw)
            print(f"\n\n\n\n<-----------this is successfully sigup--->>{students_registration}\n\n\n\n")
        return request.render('manthan.user_signup')

    @http.route('/login', type='http', auth='public', website=True)
    def student_login_pages(self, **kw):
        if request.httprequest.method == 'POST':
            students_details = request.env['student.student'].sudo().search(
                ['&', ('student_email', '=', kw['student_email']), ('student_password', '=', kw['student_password'])])
            if students_details:
                print("\n\n\n\n<-----------this is successfully LOgin--->>\n\n\n\n")
                request.session.uids = students_details.id
                print(f"\n\n\n\n<-----------this is session id -->>{request.session.uids}\n\n\n\n")
                return request.redirect('/homepage')
            else:
                print("\n\n\n\n<-----------this is NOTTTT successfully LOgin--->>\n\n\n\n")
        return request.render('manthan.user_login')

    @http.route('/logout', type='http', auth='public', website=True)
    def student_logout(self):
        request.session.logout(keep_db=True)
        print("\n\n\n\n<<<----------successfully logges out--->>>\n\n\n\n")
        return request.redirect('/homepage')


class Website_task_inherit(CustomerPortal):
    MANDATORY_BILLING_FIELDS = ["name", "phone", "email", "street", "city", "country_id", 'profession']
    OPTIONAL_BILLING_FIELDS = ["zipcode", "state_id", "vat", "company_name"]


# this code is used for having the change in the website my/acount from backend of partner model
class WebsiteUpdate(CustomerPortal):
    @route(['/my/account'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):
        if request.httprequest.method == 'POST':
            print(f"\n\n\n {post.get('profession')} \n\n\n")
            acc_rec = super(WebsiteUpdate, self).account()
            acc_rec.qcontext['partner'].update(
                {'profession': post.get('profession')})
            print(f"\n\n\n {acc_rec.qcontext['partner']['profession']} \n\n\n")
            return acc_rec
        else:
            acc_rec = super(WebsiteUpdate, self).account()
            acc_rec.qcontext['partner'].update({
                'profession': request.env.user.profession
            })
            print(f"\n\n\n {acc_rec.qcontext['partner']['profession']} \n\n\n")
            return acc_rec

    # this code is for showing the count in the website home page for student
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        Student = request.env['student.student']
        if 'student_counts' in counters:
            values['student_counts'] = Student.search_count(
                [('login_user', '=', request.env.user.id)]) if Student.check_access_rights('read',
                                                                                           raise_exception=False) else 0
        return values

    @http.route(['/my/students', '/my/students/page/<int:page>'], type='http', auth="user", website=True)
    def students_details_site(self):
        student_data = request.env['student.student']
        print(f"\n\n\n\n\n <------this is all the student ---->>{student_data}\n\n\n\n\n")
        print(f"\n\n\n\n\n <------this is all users---->>{request.env.user.name}\n\n\n\n\n")
        return request.redirect('/home')
