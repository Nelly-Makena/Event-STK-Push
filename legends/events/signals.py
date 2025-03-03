from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MpesaTransaction,EventRegistration
from django.core.mail import send_mail
from django.conf import settings

Email_Password = settings.EMAIL_HOST_PASSWORD
@receiver(post_save, sender=MpesaTransaction)
def send_email_on_transaction_save(sender, instance, created, **kwargs):
    if created:
        print("Signal triggered")
        print("EMAIL_HOST_PASSWORD",Email_Password)

        if instance.event_registration:
            recipient_email = instance.event_registration.email
            print("This is the recipient email", recipient_email)
            subject = "Transaction Confirmation"
            message = f"Dear {instance.event_registration.name},\n\nYour M-Pesa transaction of KSh {instance.Amount} was successful. We are glad to have you join us.. Thank you!"
            from_email = settings.EMAIL_HOST_USER

            try:
                send_mail(subject, message, from_email, [recipient_email])
                print(f"Email sent to {recipient_email}")
            except Exception as e:
                print(f"Failed to send email: {e}")








