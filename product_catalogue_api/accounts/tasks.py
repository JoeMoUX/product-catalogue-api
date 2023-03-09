from celery import shared_task
from django.core.mail import EmailMessage

@shared_task(bind=True)
def send_email(self, data):
  email = EmailMessage(
      subject=data['email_subject'], body=data['email_body'], to=[data['to_email']]
    )
  email.send()
  return {'message': 'Done'}
