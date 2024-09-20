from django.db import models

from base.helpers.named_date_time_model import NamedDateTimeModel


class MessageModel(NamedDateTimeModel):
    topic = models.ForeignKey('forum.TopicModel', on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()


    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.content