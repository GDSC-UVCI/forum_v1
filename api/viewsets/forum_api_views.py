from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers.forum_serializer import ForumSerializer
from api.serializers.topic_serializer import TopicSerializer
from forum.models.forum_model import ForumModel


class ForumViewSet(viewsets.ModelViewSet):
    serializer_class = ForumSerializer
    queryset = ForumModel.objects.all()

    @action(detail=True, methods=['get'])
    def topics(self, request, pk=None):
        forum = self.get_object()
        topics = forum.topics.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)