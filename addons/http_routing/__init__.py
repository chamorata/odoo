# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.http import request
from . import controllers
from . import models


def _post_init_hook(env):
    if request:
        request.is_frontend = False
        request.is_frontend_multilang = False
