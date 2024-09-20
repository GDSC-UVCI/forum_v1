from forum.models.message_model import MessageModel
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = '__all__'