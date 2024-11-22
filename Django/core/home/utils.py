from django.core.mail import send_mail

from django.conf import settings

def send_email_to_client():
    subject='This is mail from django server'
    message='TEst email'
    from_email=settings.EMAIL_HOST_USER
    recipint_list=['rahulalatre101@gmail.com']
    send_mail(subject, message, from_email, recipint_list)
    