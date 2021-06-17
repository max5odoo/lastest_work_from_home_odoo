from odoo import http, _
from odoo.http import request
from odoo.tools import groupby as groupbyelem
from operator import itemgetter
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager

from odoo.osv.expression import OR
import base64



class StudentDetail(http.Controller):
    @http.route(['/hello-world','/hello-world/<string:data>'], type='http', auth='public', website=True)
    def render_example_page(self,data="All"):
      return http.request.render('dhruv_main.hello_world_page', {'data' : data})
      # return http.Response(f'<title> Hello World </title> <h1>Hello World {data} 🙂😎🙂!!! </h1> ')


    @http.route('/student-registration', type='http', auth='public',csrf=False, website=True)
    def student_page(self,**kw):
        if request.httprequest.method == 'POST':
            print(f"\n\n\n student reg data : {kw} \n\n\n")
            vals = {
                'name' : kw['name'],
                'email_id' : kw['email'],
                'password' : kw['password'],
            }
            student_data = request.env['school.student.detail'].sudo().create(vals)
            print("\n\n\n registration successfully done... \n\n\n")

        return http.request.render('dhruv_main.student_registration_page')
        # return http.Response(f'<title> Hello World </title> <h1>Hello World {data} 🙂😎🙂!!! </h1> ')

    
    @http.route('/homepage', type='http', auth='public', website=True)
    def home_page(self):
        st_id = request.session.s_uid
        st_rec = request.env['school.student.detail'].sudo().browse([st_id])
        return http.request.render('dhruv_main.homePage',{'st_user': st_rec })

    @http.route(['/my/students','/my/students/page/<int:page>'], type='http', auth='public', website=True)
    def students(self, page=1,sortby=None,groupby=None,search=None,search_in='name', **kw):
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

        domain = [('login_user' ,'=' ,request.env.user.id)]
            
        if search and search_in:
            search_domain = []
            if search_in in ('name', 'all'):
                search_domain = OR([search_domain, [('name', 'ilike', search)]])
            if search_in in ('email_id', 'all'):
                search_domain = OR([search_domain, [('email_id', 'ilike', search)]])
            domain += search_domain  
              
        st_cnt = request.env['school.student.detail'].sudo().search_count(domain)

        # pager
        pager = portal_pager(
            url="/my/students",
            url_args={'sortby': sortby,'groupby': groupby},
            total=st_cnt,
            page=page,
            step=5
        )

        # students_data = request.env['school.student.detail'].sudo().search()
        # print(f"\n\n\n {students_data} \n\n\n")
        st_id = request.session.s_uid
        # st_rec = request.env['school.student.detail'].sudo().browse([st_id]) 
        st_rec = request.env['school.student.detail'].sudo().search(domain,order=sort_order, limit=5,offset=pager['offset']) 
        print(f"\n\n\n student recs :  {st_rec} \n\n\n")
        
        if groupby == 'gender':
            for k, g in groupbyelem(st_rec, itemgetter('gender')):
                print(f"\n\n\n {k} : {g} \n\n\n")
            grouped_student_rec = [request.env['school.student.detail'].concat(*g) for k, g in groupbyelem(st_rec, itemgetter('gender'))]
            print(f"\n\n\n g_s : {grouped_student_rec} \n\n\n")
        else:
            grouped_student_rec = [st_rec]

            

        values.update({
            'students_data': st_rec,
            'grouped_student_rec' : grouped_student_rec,
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
        return http.request.render('dhruv_main.portal_my_student',values)

    @http.route(['/student/<int:student_id>'], type='http', auth="public", website=True)
    def student(self, student_id, **kw):
      # return http.Response(f'student id :  {student_id} 🙂!!! </h1> ')
      student_rec = request.env['school.student.detail'].browse([student_id])
      values = {}
      values.update({
        'id' : student_id,
        'student' : student_rec
        })
      return http.request.render('dhruv_main.student_portal_template',values)

    
    @http.route(['/course/<int:course_id>'], type='http', auth="public", website=True)
    def course(self, course_id, **kw):
      # return http.Response(f'course id :  {course_id} 🙂!!! </h1> ')
      course_rec = request.env['courses.detail'].browse([course_id])
      values = {}
      values.update({
        'id' : course_id,
        'course' : course_rec
        })
      return http.request.render('dhruv_main.course_portal_template',values)




    @http.route('/student-login', type='http', auth='public',csrf=False,website=True)
    def login_page(self,**kw):
        alert_msg = None
        if request.httprequest.method == 'POST':
            print(f"\n\n\n student login data : {kw} \n\n\n")
            student_search_dt = request.env['school.student.detail'].sudo().search(['&',('email_id','=',kw['email']),('password','=',kw['password'])])
            if student_search_dt:
                request.session.s_uid = student_search_dt.id
                print("\n\n\n login successfully done... \n\n\n")
                return request.redirect('/homepage')
            else:
                alert_msg = 'Email ID & Password wrong...'
                print("\n\n\n login successfully not done... email and password wrong... \n\n\n")
        return http.request.render('dhruv_main.student_login_page',{'alert_msg':alert_msg})
    
    @http.route('/student-logout', type='http', auth='public', website=True)
    def logout_page(self):
        request.session.logout(keep_db=True)
        return request.redirect('/homepage')

    @http.route('/student-profile', type='http', auth='public', website=True)
    def v_profile_page(self):
        if not request.session.s_uid:
            return request.redirect('/homepage')
        student_profile_rec = request.env['school.student.detail'].sudo().browse(request.session.s_uid) 
        st_id = request.session.s_uid
        st_rec = request.env['school.student.detail'].sudo().browse([st_id])  
        return http.request.render('dhruv_main.student_vprofile_page',{'student_dt':student_profile_rec,'st_user': st_rec})

    @http.route('/my/students/add', type='http', auth='public', website=True)
    def add_student(self,redirect=None,**post):
        if request.httprequest.method == 'POST':
            cnt = post.get('record_cnt')

            print(f"\n\n\n {cnt} \n\n\n") 
            for i in range(0,int(cnt)):
                name = f'course{i+1}'
                print(f"\n\n\n course name {i+1} :  {post.get(name)} \n\n\n")
                name = f'created_by{i+1}'
                print(f"\n\n\n created_by {i+1} :  {post.get(name)} \n\n\n")
                name = f'desc{i+1}'
                print(f"\n\n\n desc {i+1} :  {post.get(name)} \n\n\n")

            
            #create record on main course and get ids of created record
            course_ids = []
            for i in range(0,int(cnt)):

                course_key_name = f'course{i+1}'
                created_by_key_name = f'created_by{i+1}'
                desc_key_name = f'desc{i+1}'

                vals = {
                    'name' :  post.get(course_key_name),
                    'short_desc' : post.get(created_by_key_name),
                    'created_by' : post.get(desc_key_name)
                }

                course = request.env['courses.detail'].create(vals)
                course_ids.append(course)

            
            print(f"n\n\n {course} \n\n\n")







                
            avatar_img = post.get('avatar_img').read()
            print(f"\n\n\n {post['gender']} \n\n\n") 
            vals = {
                'name' : post.get('name'),
                'email_id' : post.get('email_id'),
                'gender' : post.get('gender'),
                'address_line1': post.get('address_line1'),
                'login_user' : request.env.user.id,
                'avatar_img' : base64.b64encode(avatar_img)
            }
            student = request.env['school.student.detail'].create(vals)



            #now add 1 one course record to course one2many in student model
            for course_id in course_ids:
                print(f"\n\n\n {course_id} \n\n\n")
                student.write({
                        'course_ids' : [(0, 0 ,{
                                'course_id' : course_id.id
                            })]
                    })
            print("student added successfully :)")
            return request.redirect("/my/students")

        print("get request...")    
        return http.request.render('dhruv_main.portal_add_student')
        

            




  

