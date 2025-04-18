from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task(bind=True)
def send_email_task(self,to,subject,message,html_message):
    send_mail(
                subject=subject,
                message="welcome",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=to,
                fail_silently=False,
                html_message=html_message
            )