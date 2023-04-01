from django.core.mail import send_mail
from celery import shared_task

from account.models import User

@shared_task()
def send_subscription_mail():
    for contact in User.objects.all():
        send_mail(
            'Your weekly subscription',
            'We will send you our spam every week',
            'info@ecommerce.com',
            [contact.email],
            fail_silently=False
        )