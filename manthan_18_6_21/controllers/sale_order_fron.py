from odoo import http
from odoo.http import request


class Registration_sale_route(http.Controller):
    @http.route('/register/sale/prac', type='http', auth='public', website=True)
    def sale_registration(self):
        return http.request.render('manthan_18_6_21.sale_order_front')


class Final_sale_route(http.Controller):
    @http.route('/sale_front/form/submit', type='http', auth='public', website=True)
    def sale_post_data(self, **post):
        end_date_data = post['end_date']
        start_date_data = post['start_date']
        state_data = post['state']
        if state_data == 'all':
            sale_details = request.env['sale.order'].sudo().search(
                [('date_order', '>=', start_date_data), ('date_order', '<=', end_date_data)])
        else:
            sale_details = request.env['sale.order'].sudo().search(
                [('date_order', '>=', start_date_data), ('date_order', '<=', end_date_data),
                 ('state', '=', state_data)])
        vals = {
            'sale_details': sale_details,
        }
        return request.render("manthan_18_6_21.sale_order_list_page", vals)

    @http.route('/sale/all/data/<int:so_id>', type='http', auth='public', website=True)
    def sale_data_all(self, so_id):
        sale_records = request.env['sale.order'].browse([so_id])
        values = {}
        values.update({
            'sale_order': sale_records
        })
        return request.render('manthan_18_6_21.sale_order_detail_page', values)
