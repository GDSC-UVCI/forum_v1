from rest_framework import viewsets

from api.serializers.message_serializer import MessageSerializer
from forum.models.message_model import MessageModel


class MessageViewsets(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = MessageModel.objects.all()