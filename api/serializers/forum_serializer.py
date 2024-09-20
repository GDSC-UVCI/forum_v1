from forum.models.forum_model import ForumModel
from rest_framework import serializers

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumModel
        fields = '__all__'