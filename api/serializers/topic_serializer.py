from forum.models.topic_model import TopicModel
from rest_framework import serializers


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicModel
        fields = '__all__'
