from django.core.mail import send_mail
from celery import shared_task
from .models import User

@shared_task
def send_beat_email():
    for contact in User.objects.all():
        send_mail(
            f'Your are subscribed',
            f'Thank you! Here is your offers of our e-store',
            'support@example.com',
            [contact.email],
            fail_silently=False,
        )
