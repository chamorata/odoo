# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.mail.controllers import thread

from odoo.http import request, route


class ThreadController(thread.ThreadController):
    @route()
    def mail_message_post(self, thread_model, thread_id, post_data, context=None, **kwargs):
        if selected_answer_id := kwargs.pop("selected_answer_id", None):
            request.update_context(selected_answer_id=selected_answer_id)
        return super().mail_message_post(thread_model, thread_id, post_data, context, **kwargs)
