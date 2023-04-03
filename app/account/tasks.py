from django.core.mail import send_mail
from celery import shared_task

@shared_task()
def send_confirmation_email_task(email, confirm_link):
    send_mail(
        subject='Please confirm your registration',
        message=f'follow this link {confirm_link} \n'
                  f'to confirm',
        from_email='support@ecommerce.com',
        recipient_list=[email, ]
    )