from django.core.mail import send_mail
from celery import shared_task

from account.models import User


@shared_task()
def send_subscription_mail_task():
    for user in User.objects.all():
        send_user_email_task.delay(user.email)


@shared_task()
def send_user_email_task(email):
    send_mail(
        'Your weekly subscription',
        'We will send you our spam every week',
        'info@ecommerce.com',
        [email],
        fail_silently=False
    )

