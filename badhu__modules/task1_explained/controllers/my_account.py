from odoo import http, _
from odoo.http import request
from odoo.exceptions import AccessError, MissingError
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager


class MyHomeInherit(CustomerPortal):
    MANDATORY_BILLING_FIELDS = ["name", "phone", "email", "street", "city", "country_id", "is_student"]
    OPTIONAL_BILLING_FIELDS = ["zipcode", "state_id", "vat", "company_name"]

    _items_per_page = 5

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)

        Student = request.env['student.details']
        if 'student_count' in counters:
            values['student_count'] = Student.search_count([]) if Student.check_access_rights('read', raise_exception=False) else 0
        return values

    def _student_get_page_view_values(self, student, access_token, **kwargs):
        values = {
            'page_name': 'students',
            'student': student,
        }

        print('_student_get_page_view_values', values)
        return self._get_page_view_values(student, access_token, values, 'my_student_history', False, **kwargs)

    @http.route(["/my/students/<model('student.details'):student>"], type='http', auth="public", website=True)
    def portal_student_page(self, student=None, access_token=None, **kw):
        try:
            student_sudo = self._document_check_access('student.details', student.id, access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        values = self._student_get_page_view_values(student, access_token, **kw)
        values['students'] = request.env['student.details'].search([('name', '=', student.name.name)])

        return request.render('task1_explained.student_report_onclick_', values)

    @http.route(['/students', '/my/students', '/my/students/page/<int:page>'], type='http', auth='public', website=True)
    def student_info(self,  page=1, date_begin=None, date_end=None, sortby=None, **kwargs):
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        student = request.env['student.details']

        searchbar_sortings = {
            'name': {'label': _('Name'), 'order': 'name'},
            'dob': {'label': _('Birth Date'), 'order': 'dob desc'},
            'create_date': {'label': _('Created Date'), 'order': 'create_date desc'},
        }

        # default sortby order
        if not sortby:
            sortby = 'name'
        sort_order = searchbar_sortings[sortby]['order']

        # content according to pager
        student_count = student.search_count([])

        pager = portal_pager(
            url="/my/students",
            url_args={'sortby': sortby},
            total=student_count,
            page=page,
            step=self._items_per_page
        )
        domain = []
        students = student.search(domain, order=sort_order, limit=self._items_per_page, offset=pager['offset'])
        request.session['my_student_history'] = students.ids[:100]
        values.update({
            'students': students.sudo(),
            'page_name': 'student',
            'pager': pager,
            'default_url': '/my/students',
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
        })
        # response = request.render("task1_explained.student_site_template", values)
        # response.headers['X-Frame-Options'] = 'DENY'
        # return response
        return request.render("task1_explained.student_site_template", values)

    # @http.route(['/students', '/my/students'], auth='public', website=True)
    # def student_info(self, **kw):
        # students = request.env['student.details'].sudo().search([])
        # return request.render("task1_explained.student_site_template", {'students': students})

    @http.route(['/my/account'], type='http', auth='public', website=True)
    def account(self, redirect=None, **post):
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        values.update({
            'error': {},
            'error_message': [],
            'student':request.env.user.profession
        })
        if post and request.httprequest.method == 'POST':
            error, error_message = self.details_form_validate(post)
            values.update({'error': error, 'error_message': error_message})
            values.update(post)
            if not error:
                values = {key: post[key] for key in self.MANDATORY_BILLING_FIELDS}
                values.update({key: post[key] for key in self.OPTIONAL_BILLING_FIELDS if key in post})
                for field in set(['country_id', 'state_id']) & set(values.keys()):
                    try:
                        values[field] = int(values[field])
                    except:
                        values[field] = False
                values.update({'zip': values.pop('zipcode', '')})
                partner.sudo().write(values)
                if redirect:
                    return request.redirect(redirect)
                return request.redirect('/my/home')

        countries = request.env['res.country'].sudo().search([])
        states = request.env['res.country.state'].sudo().search([])
        is_student = request.env.user.is_student
        print(f"\n\n\n\nis_student - - - {is_student}\n\n\n")

        values.update({
            'partner': partner,
            'countries': countries,
            'states': states,
            'is_student': is_student,
            'has_check_vat': hasattr(request.env['res.partner'], 'check_vat'),
            'redirect': redirect,
            'page_name': 'my_details',
        })

        response = request.render("task1_explained.contact_field_in_website", values)
        response.headers['X-Frame-Options'] = 'DENY'
        return response

    @http.route(['/my', '/my/home'], type='http', auth="public", website=True)
    def home(self, **kw):
        values = self._prepare_portal_layout_values()
        return request.render('task1_explained.my_account_student', values)
