# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.payment import setup_provider, reset_payment_provider

from . import controllers
from . import models


def post_init_hook(env):
    setup_provider(env, 'worldline')


def uninstall_hook(env):
    reset_payment_provider(env, 'worldline')
