from operator import itemgetter
from odoo.http import request
from odoo.exceptions import AccessError, UserError, AccessDenied, ValidationError
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import route, Controller
from odoo import fields, _, tools
from odoo.tools import groupby as groupbyelem
from odoo.osv.expression import OR
import base64


class HomePage(Controller):

    @route(['/homepage', '/homepage/<string:data>'], type='http', auth='public', website=True)
    def home_page(self, **kw):
        all_user = request.env["student.data"].sudo().search(
            [])
        if request.httprequest.method == 'POST':
            for users in all_user:
                if users.email == kw['lemail']:
                    print(f"\n\n\n{users.first_name}\n\n\n")
                    print(users)
                    if users.password == kw['lpass']:
                        request.session.uids = users.id
                        return request.render('student_app.homepage_web', {'users': users})
                    else:
                        return request.render('student_app.login_page', {'msg': 'hi how are you'})
        else:
            users = request.env["student.data"].sudo().browse(
                [request.session.uids])
            return request.render('student_app.homepage_web', {'users': users})

    @route('/login', type='http', auth='public', website=True)
    def login_form(self, **kw):
        return request.render('student_app.login_page', {})

    @route('/signup', type='http', auth='public', website=True)
    def signup_form(self, **kw):
        print('\n\n\n\nsignup\n\n\n\n')
        if request.httprequest.method == 'POST':
            student = request.env['student.data'].sudo().create(
                {
                    'first_name': kw['first_name'],
                    'last_name': kw['last_name'],
                    'email': kw['semail'],
                    'password': kw['spass'],
                }
            )
            return request.redirect('/homepage')

        else:
            return request.render('student_app.signup_page')
        # Create user.
        # user = cls.env['res.users'].create({
        #     'name': 'Because I am accountman!',
        #     'login': 'accountman',
        #     'password': 'accountman',
        #     'groups_id': [(6, 0, cls.env.user.groups_id.ids), (4, cls.env.ref('account.group_account_user').id)],
        # })

    @route('/logout', type='http', auth='public', website=True)
    def logout(self, **kw):
        request.session.logout(keep_db=True)
        return request.redirect('/homepage')

    @route('/profile', type='http', auth='public', website=True)
    def profile(self, **kw):
        print(f"\n\n\n{request.session.uids}\n\n\n")
        if request.session.uids is not None:
            users = request.env["student.data"].sudo().browse(
                [request.session.uids])
            return request.render('student_app.profile_page', {'users': users})
        else:
            return request.redirect('/homepage')

    @route('/index', type='http', auth='public', website=True)
    def index(self, **kw):
        return request.render('student_app.homepage')


class PortalUpdate(CustomerPortal):
    @route(['/my/account'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):
        print(f"\n\n\n\nhiiidekho\n\n\n")
        print(f"\n\n\n\n{post.get('profession')}\n\n\n")
        acc = super(PortalUpdate, self).account(
        )
        acc.qcontext['partner'].update(
            {'profession': post.get('profession')})
        # values.update({'profession': post.get('profession')})
        # partner.sudo().write(values)
        return acc

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)

        if 'student_counts' in counters:
            # values['student_counts'] = request.env["student.data"].sudo().search_count(
            #     [])
            professors = request.env['res.user'].search[(
                'name', '=', 'Professor')]
            for professor in professors:

                values['student_counts'] = request.env["student.data"].sudo().search_count(
                    [("login_user", "=", request.env.user.id)])
        return values

    @route(['''/my/student''',
            '''/my/student/page/<int:page>'''
            ], type='http', auth="user", website=True)
    def student_page(self,  page=1, sortby=None, groupby=None, search=None, search_in='first_name', ** post):
        values = {}
        partner = request.env.user.partner_id

        searchbar_inputs = {
            'first_name': {'input': 'first_name', 'label': _('Search by firstname')},
            'last_name': {'input': 'last_name', 'label': _('Search by lastname')},
            'all': {'input': 'all', 'label': _('Search in All')},

        }

        ################### shorting of order ##################

        searchbar_sortings = {
            'first_name': {'label': _('Name'), 'order': 'first_name'},
            'age': {'label': _('Age'), 'order': 'age'},
        }

        ######################## Group filter ##################

        searchbar_groupby = {
            'none': {'input': 'none', 'label': _('None')},
            'gender': {'input': 'gender', 'label': _('Gender')},

        }

        # default short
        if not sortby:
            sortby = 'first_name'
        search_order = searchbar_sortings[sortby]['order']

        if not groupby:
            groupby = 'gender'
        domain = [('login_user', '=', request.env.user.id)]
        # search

        if search and search_in:
            search_domain = []
            if search_in in ('first_name', 'all'):
                search_domain = OR(
                    [search_domain, [('first_name', 'ilike', search)]])
            if search_in in ('last_name', 'all'):
                search_domain = OR(
                    [search_domain, [('last_name', 'ilike', search)]])
            domain += search_domain
            print(domain, search_domain)
        # search method ready search length for pager # student count

        student = request.env["student.data"].sudo().search(
            domain)
        student_count = len(student)

        ################## pager ##############################

        limits = 4  # limit for view record
        pager = request.website.pager(
            url='/my/student',
            page=page,
            total=student_count,
            step=limits,
            url_args={'sortby': sortby}
        )

        ################## login orofessor or student condition ##############################

        student = request.env["student.data"].sudo().search(
            domain, order=search_order, limit=limits, offset=pager['offset'])

        # print(f"\n\n\n\n\n\n{grouped_student}\n\n\n\n\n")
        if groupby == 'gender':
            grouped_student = [request.env['student.data'].concat(
                *g) for k, g in groupbyelem(student, itemgetter('gender'))]
            # for groups in grouped_student:
            #     print(f"\n\n\n\n\n{groups[0].sudo().gender}\n\n\n\n\n")
        else:
            grouped_student = [student]

        ######################## value update ##################
        # for ui bar only
        values.update({
            'searchbar_sortings': searchbar_sortings,
            'default_url': '/my/student',
            'pager': pager,
            'sortby': sortby,
            'groupby': groupby,
            'grouped_student': grouped_student,
            'searchbar_groupby': searchbar_groupby,
            'searchbar_inputs': searchbar_inputs,
            'search_in': search_in,
            'search': search,
        })

        return request.render("student_app.portal_students", values)

    @route(['''/my/student/<int:student_id>'''
            ], type='http', auth="user", website=True)
    def current_student(self, student_id=None, course_id=None, ** post):
        values = {}
        student = request.env["student.data"].sudo().browse([student_id])
        request.session.uids = student_id
        values.update({'student': student})
        return request.render("student_app.portal_student_view", values)

    @route(['''/my/student/course/<int:course_id>'''
            ], type='http', auth="user", website=True)
    def course_page(self, course_id=None, **post):
        values = {}
        user = request.session.uids
        course = request.env["courses.data"].sudo().browse([course_id])
        values.update({'course': course, 'user': user})
        return request.render("student_app.portal_course_view", values)

    def checkout_form_validate(self, data):
        error = {}
        error_message = {}

        if not data.get('firstname'):
            error["firstname"] = 'error'
            error_message["firstname"] = 'please enter your name'

        if not data.get('lastname'):
            error["lastname"] = 'error'
            error_message["lastname"] = 'please enter your surname'

        if not data.get('email'):
            error["email"] = 'error'
            error_message['email'] = 'please enter your email'

        if data.get('email') and not tools.single_email_re.match(data.get('email')):
            error["email"] = 'error'
            error_message['email'] = 'Invalid Email! Please enter a valid email address.'

        # # Validation
        # for field_name in self.MANDATORY_BILLING_FIELDS:
        #     if not data.get(field_name):
        #         error[field_name] = 'missing'
        #  # error message for empty required fields
        # if [err for err in error.values() if err == 'missing']:
        #     error_message.append(_('Some required fields are empty.'))
        print(f"\n\n\n{error}\n\n\n{error_message}")
        return error, error_message

    @route(['''/my/signup'''
            ], type='http', methods=['GET', 'POST'], auth="public", website=True)
    def signup(self, **post):
        print(f"\n\n\n\n{post}\n\n\n\n\n")
        student_courses = request.env["courses.data"].search([])
        values = {}
        values.update({
            'error': {},
            'error_message': {},
            'student_courses': student_courses,
        })

        if request.httprequest.method == 'POST':
            lines_vals = []
            for i in range(1, int(post.get('total_row'))+1):

                courses_name = post.get(f'course{i}')
                course_rec = request.env['courses.data'].search(
                    [('course_names', '=', courses_name)])
                print(f"\n\n\n\n\n{courses_name}\n\n\n\n")
                # ----------by using create 0,0
                if course_rec:
                    lines_vals.append((0, 0, {
                        'course_id': course_rec.id,

                        'course_amount': 500,
                    }))

            # print(f"\n\n\n\n{post}\n\n\n\n\n")
            # courses_rec=self.env["student.data.lines"].browse([post.get('course')])
            if not post.get('photos'):
                error, error_message = self.checkout_form_validate(post)
                if not error:
                    print(lines_vals)
                    img = post.get('photos')
                    imgs = img.read()
                    student = request.env['student.data'].sudo().create(
                        {
                            'first_name': post.get('firstname'),
                            'last_name': post.get('lastname'),
                            'email': post.get('email'),
                            'gender': post.get('gender'),
                            'photo_id': base64.b64encode(imgs),
                            'student_line_ids': lines_vals,


                        }
                    )
                    return request.redirect('/my/student')
                else:
                    values.update(
                        {
                            'error': error,
                            'error_message': error_message,
                        }
                    )
                    return request.render("student_app.portal_signup_form", values)
            else:
                return "please upload image"
        else:

            return request.render("student_app.portal_signup_form", values)
