# from django.shortcuts import render

from rest_framework import viewsets
from .models import Client, Dispatch, Message
from .serializers import ClientSerializer, DispatchSerializer, MessageSerializer, MsgSerializer

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class DispatchViewSet(viewsets.ModelViewSet):
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer

    def perform_create(self, serializer):
        dispatch = serializer.save()
        self.send_messages(dispatch)

    def send_messages(self, dispatch):
        clients = Client.objects.filter(dispatch.client_filter)

        for client in clients:
            # Отправка сообщения через Celery
            send_email_task.delay(client.email, dispatch.message)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

def some_view(request):
    # Логика представления
    process_message_task.delay()
    return HttpResponse('Задача по обработке сообщения запущена.')

# интеграция c API
class SendMessageView(APIView):
    def post(self, request, msg_id):
        serializer = MsgSerializer(data=request.data)
        if serializer.is_valid():
            token = 'token_token' # Замените на актуальный токен
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }

            return Response({'message': 'Сообщение успешно отправлено'})
        else:
            return Response(serializer.errors, status=400)
