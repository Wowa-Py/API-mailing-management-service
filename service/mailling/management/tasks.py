from celery import shared_task
from django.core.mail import send_mail
from .models import Message


@shared_task
def send_email_task(email, message):
    try:
        # Отправка электронной почты
        send_mail(
            'Subject',
            message,
            'from@example.com',
            [email],
            fail_silently=False,
        )

        # Сохранение статуса отправки в модели Message
        message_obj = Message.objects.get(email=email)
        message_obj.status = 'Отправлено'
        message_obj.save()
    except Exception as e:
        # Обработка ошибок
        message_obj = Message.objects.get(email=email)
        message_obj.status = 'Ошибка'
        message_obj.save()
        raise e
