from rest_framework import serializers
from .models import Client, Dispatch, Message

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class DispatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispatch
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

from rest_framework import serializers

class MsgSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    phone = serializers.IntegerField()
    text = serializers.CharField()
