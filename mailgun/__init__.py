__title__ = 'mailgun'
__version__ = '0.0.1'
__author__ = 'Stephen Hamer'
__license__ = 'Apache 2.0'

import base64
import email

import mailgun2

class MailgunError(Exception):
    pass


class Mailgun:
    api_key = None
    validation_key = None
    domain = 'forum.upverter.com'
    client = None

    @staticmethod
    def init(api_key, validation_key=None, domain=None):
        Mailgun.api_key = api_key
        Mailgun.validation_key = validation_key
        if domain:
            Mailgun.domain = domain
        Mailgun.client = mailgun2.Mailgun(Mailgun.domain, Mailgun.api_key, Mailgun.validation_key)


class MailgunMessage:

    '''
    def send_message(self, from_email, to, cc=None, bcc=None,
                     subject=None, text=None, html=None, user_variables=None,
                     reply_to=None, headers=None, inlines=None,
                     attachments=None, campaign_id=None, tags=None):
    '''

    @classmethod
    def send_raw(cls, sender, recipients, mime_body, servername=''):
        msg = email.message_from_string(mime_body)

        text_body = None
        html_body = None

        payloads = msg.get_payload()
        for payload in payloads:
            encoding = payload.get('Content-Transfer-Encoding', 'unknown')
            if encoding != 'base64':
                raise MailgunError('message not base64 encoded: %s' % (encoding, ))
            body = base64.decodestring(payload.get_payload())

            content_type = payload.get('Content-Type', 'none')
            if content_type.startswith('text/plain'):
                text_body = body
            elif content_type.startswith('text/html'):
                html_body = body
            else:
                raise MailgunError('unexpected content type for payload: %s' % (content_type, ))

        Mailgun.client.send_message(sender, recipients, subject=msg.get('Subject'), text=text_body, html=html_body)


    @classmethod
    def send_txt(cls, sender, recipients, subject, text, servername='', options=None):
        Mailgun.client.send_message(sender, recipients, subject=subject, text=text)
