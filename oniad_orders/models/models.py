# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class oniad_orders(models.Model):
#     _name = 'oniad_orders.oniad_orders'
#     _description = 'oniad_orders.oniad_orders'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class oniad_orders(models.Model):
    _name = 'oniad_orders.oniad_orders'
    _description = 'oniad_orders.oniad_orders'

    name = fields.Char()
    total = fields.Integer()
    description = fields.Text()