from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User

def send_contact_email_message(subject, email, content, ip, user_id):
    user = User.objects.get(id=user_id) if user_id else None
    message = render_to_string('feedback_templates/email/feedback_email_send.html', {
        'email': email,
        'content': content,
        'ip': ip,
        'user': user,
    })
    email_message = EmailMessage(subject, message, settings.EMAIL_HOST_USER, settings.EMAIL_ADMIN)
    email_message.send(fail_silently=False)