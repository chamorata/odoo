# -*- coding: utf-8 -*-

from odoo import fields, models


class ResUsersLog(models.Model):
    _inherit = 'res.users.log'

    create_uid = fields.Integer(index=True)
    ip = fields.Char(string="IP Address")
