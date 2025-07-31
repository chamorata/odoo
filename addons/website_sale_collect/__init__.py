# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.payment import reset_payment_provider

from . import controllers
from . import models
from . import utils


def uninstall_hook(env):
    reset_payment_provider(env, 'custom', custom_mode='on_site')
