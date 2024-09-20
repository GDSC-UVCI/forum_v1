from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers.message_serializer import MessageSerializer
from api.serializers.topic_serializer import TopicSerializer
from forum.models.topic_model import TopicModel


class TopicViewSet(viewsets.ModelViewSet):
    queryset = TopicModel.objects.all()
    serializer_class = TopicSerializer

    @action(detail=True, methods=['get'])
    def messages(self, request, pk=None):
        topic = self.get_object()
        messages = topic.messages.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)