@http.route(['/my/students', '/my/students/page/<int:page>'], type='http', auth='public', website=True)
def students(self, page=1, sortby=None, groupby=None, search=None, search_in='name', **kw):
    values = {}
    searchbar_sortings = {
        'name': {'label': _('Name'), 'order': 'name'},
        'email_id': {'label': _('Email'), 'order': 'email_id desc'}
    }

    searchbar_inputs = {
        'name': {'input': 'name', 'label': _('Search by Name')},
        'email_id': {'input': 'email_id', 'label': _('Search by Email')},
        'all': {'input': 'all', 'label': _('Search in All')},

    }

    searchbar_groupby = {
        'none': {'input': 'none', 'label': _('None')},
        'gender': {'input': 'gender', 'label': _('Gender')},

    }

    if not sortby:
        sortby = 'name'
    sort_order = searchbar_sortings[sortby]['order']

    if not groupby:
        groupby = 'gender'

    domain = [('login_user', '=', request.env.user.id)]

    if search and search_in:
        search_domain = []
        if search_in in ('name', 'all'):
            search_domain = OR(
                [search_domain, [('name', 'ilike', search)]])
        if search_in in ('email_id', 'all'):
            search_domain = OR(
                [search_domain, [('email_id', 'ilike', search)]])
        domain += search_domain

        st_cnt = request.env['school.student.detail'].sudo(
        ).search_count(domain)

        # pager
        pager = portal_pager(
            url="/my/students",
            url_args={'sortby': sortby, 'groupby': groupby},
            total=st_cnt,
            page=page,
            step=5
        )

        # students_data = request.env['school.student.detail'].sudo().search()
        # print(f"\n\n\n {students_data} \n\n\n")
        st_id = request.session.s_uid
        # st_rec = request.env['school.student.detail'].sudo().browse([st_id])
        st_rec = request.env['school.student.detail'].sudo().search(
            domain, order=sort_order, limit=5, offset=pager['offset'])
        print(f"\n\n\n student recs :  {st_rec} \n\n\n")

        if groupby == 'gender':
            for k, g in groupbyelem(st_rec, itemgetter('gender')):
                print(f"\n\n\n {k} : {g} \n\n\n")
            grouped_student_rec = [request.env['school.student.detail'].concat(
                *g) for k, g in groupbyelem(st_rec, itemgetter('gender'))]
            print(f"\n\n\n g_s : {grouped_student_rec} \n\n\n")
        else:
            grouped_student_rec = [st_rec]

        values.update({
            'students_data': st_rec,
            'grouped_student_rec': grouped_student_rec,
            'page_name': 'student',
            'default_url': '/my/students',
            'pager': pager,
            'sortby': sortby,
            'groupby': groupby,
            'searchbar_sortings': searchbar_sortings,
            'searchbar_inputs': searchbar_inputs,
            'search_in': search_in,
            'search': search,
            'searchbar_groupby': searchbar_groupby,

        })
        return http.request.render('new_app.portal_my_student', values)
