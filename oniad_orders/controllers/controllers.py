# -*- coding: utf-8 -*-
# from odoo import http


# class OniadOrders(http.Controller):
#     @http.route('/oniad_orders/oniad_orders/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oniad_orders/oniad_orders/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oniad_orders.listing', {
#             'root': '/oniad_orders/oniad_orders',
#             'objects': http.request.env['oniad_orders.oniad_orders'].search([]),
#         })

#     @http.route('/oniad_orders/oniad_orders/objects/<model("oniad_orders.oniad_orders"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oniad_orders.object', {
#             'object': obj
#         })
