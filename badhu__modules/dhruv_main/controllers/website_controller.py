
from odoo import http, _
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.exceptions import AccessError, MissingError
from odoo.http import request


class CustomerAccountU(CustomerPortal):
    # MANDATORY_BILLING_FIELDS = ["name", "phone", "email", "street", "city", "country_id","designation"]
    # OPTIONAL_BILLING_FIELDS = ["zipcode", "state_id", "vat", "company_name"]


    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)

        Student = request.env['school.student.detail'].sudo()
        if 'student_count' in counters:
            values['student_count'] = Student.search_count([]) if Student.check_access_rights('read',
                                                                                        raise_exception=False) else 0
            print(f"\n\n\n {values['student_count']} \n\n\n")                                                                                                                                                                           
        return values


    @http.route(['/my/account'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):
        if request.httprequest.method == 'POST':
            print(f"\n\n\n {post.get('designation')} \n\n\n")
            acc_rec = super(CustomerAccountU,self).account()
            acc_rec.qcontext['partner'].update(
                {'designation' : post.get('designation')})
            print(f"\n\n\n {acc_rec.qcontext['partner']['designation']} \n\n\n")
            # return acc_rec
            return request.redirect('/my/home')
        else:    
            acc_rec = super(CustomerAccountU,self).account()
            acc_rec.qcontext['partner'].update({
                    'designation' : request.env.user.designation
                    })
            print(f"\n\n\n {acc_rec.qcontext['partner']['designation']} \n\n\n")
            return acc_rec

    
    # def _prepare_portal_layout_values(self):
    #     """Values for /my/* templates rendering.

    #     Does not include the record counts.
    #     """
    #     # get customer sales rep
    #     sales_user = False
    #     partner = request.env.user.partner_id
    #     if partner.user_id and not partner.user_id._is_public():
    #         sales_user = partner.user_id

    #     return {
    #         'sales_user': sales_user,
    #         'page_name': 'home',
    #     }

    # def _prepare_home_portal_values(self, counters):
    #     """Values for /my & /my/home routes template rendering.

    #     Includes the record count for the displayed badges.
    #     where 'coutners' is the list of the displayed badges
    #     and so the list to compute.
    #     """
    #     return {}

    
    # @route(['/my', '/my/home'], type='http', auth="user", website=True)
    # def home(self, **kw):
    #     st_cnt = request.env['school.student.detail'].search_count([])
    #     values =  super(CustomerAccountU,self)._prepare_portal_layout_values()
    #     values.update({
    #         'st_cnt' : st_cnt
    #         })
    #     return request.render("portal.portal_my_home", values)    

    

            
      