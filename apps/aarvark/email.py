# ChainedInstanceCheck
# ClsInClassMethod

from django.core import mail


def check_received_mail_exists(subject, to, strings, clear_outbox=True, html_body=None):
    if not (isinstance(strings, list) or isinstance(strings, tuple)):
        strings = (strings,)
    assert len(mail.outbox) >= 1, "No mails sent"
    assert _mail_exists(subject, to, strings, html_body)
    if clear_outbox:
        mail.outbox = []


class EmailTokenBackend:
    @classmethod
    def has_exactly_one(self, model, email):
        try:
            model.objects.get(email=email)
            return True
        except (model.DoesNotExist, model.MultipleObjectsReturned):
            return False
