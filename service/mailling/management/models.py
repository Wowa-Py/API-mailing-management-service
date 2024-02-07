from django.db import models

class Client(models.Model):
    phone_number = models.CharField(max_length=11)
    mobile_operator_code = models.CharField(max_length=10)
    tag = models.CharField(max_length=255)
    timezone = models.CharField(max_length=255)

class Dispatch(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    message = models.TextField()
    client_filter = models.Q()


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    dispatch = models.ForeignKey(Dispatch, on_delete=models.CASCADE, related_name='messages')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
