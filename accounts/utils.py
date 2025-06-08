from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

# def send_password_reset_link(user):
#     uid = urlsafe_base64_encode(force_bytes(user.pk))
#     token = default_token_generator.make_token(user)

#     reset_url = f"{settings.DOMAIN}/accounts/reset/{uid}/{token}/"

#     subject = "Welcome to TaskFlow – Set your password"
#     message = f"""
# Hello {user.name},

# Your account has been created on TaskFlow.

# To set your password and activate your access, click the link below:

# {reset_url}

# If you didn’t request this, you can ignore this email.

# Thanks,  
# TaskFlow Team
# """
#     send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])


def send_verification_email(user, action='set_password'):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    domain = settings.DOMAIN
    reset_path = reverse('accounts:reset_password_validate', kwargs={'uidb64': uid, 'token': token})
    reset_url = f"{domain}{reset_path}"

    message = render_to_string('accounts/email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
        'action': action,
    })

    email = EmailMessage(
        subject="Set your password – TaskFlow" if action != 'reset_password' else "Reset your password – TaskFlow",
        body=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email]
    )
    email.send()
