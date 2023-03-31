from django.core.mail import send_mail
from celery import shared_task

@shared_task()
def send_order_email_task(email_address, order):
    send_mail(
        "Your Order",
        f"Your order {order}. Thank you!",
        "support@example.com",
        [email_address],
        fail_silently=False,
    )