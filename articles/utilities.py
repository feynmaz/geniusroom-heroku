from django.template.loader import render_to_string
from django.core.signing import Signer
from django.core.mail import send_mail
from datetime import datetime
from os.path import splitext

from geniusroom_server_render.settings import ALLOWED_HOSTS, EMAIL_HOST_USER


signer = Signer()


def send_activation_notification(user):
    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'

    context = {
        'user': user,
        'host': host,
        'sign': signer.sign(user.username)
    }

    subject = render_to_string('main/email/activation_letter_subject.txt', context)
    body_text = render_to_string('main/email/activation_letter_content.html', context)

    send_mail(
        subject=subject,
        message='',
        html_message=body_text,
        from_email=EMAIL_HOST_USER,
        recipient_list=[user.email]
    )


def get_timestamp_path(instance, filename):
    return '%s%s' % (datetime.now().timestamp(), splitext(filename)[1])


def send_new_comment_notification(comment):
    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'
    author = comment.article.author
    context = {
        'author': author,
        'host': host,
        'comment': comment,
    }
    subject = render_to_string('main/email/new_comment_letter_subject.txt', context)
    body_text = render_to_string('main/email/new_comment_letter_body.html', context)

    send_mail(
        subject=subject,
        message='',
        html_message=body_text,
        from_email=EMAIL_HOST_USER,
        recipient_list=[author.email]
    )

