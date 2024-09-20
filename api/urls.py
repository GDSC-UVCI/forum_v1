from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.viewsets.forum_api_views import ForumViewSet
from api.viewsets.message_api_views import MessageViewsets
from api.viewsets.topic_api_views import TopicViewSet

router = DefaultRouter()
router.register(r'forums', ForumViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'messages', MessageViewsets)
ForumViewSet.http_method_names = ['get', 'post', 'head', 'options']
TopicViewSet.http_method_names = ['get', 'post', 'head', 'options']
MessageViewsets.http_method_names = ['get', 'post', 'head', 'options']

urlpatterns = [
    path('', include(router.urls))
]