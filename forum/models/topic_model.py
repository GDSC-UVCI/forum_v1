from django.db import models

from base.helpers.named_date_time_model import NamedDateTimeModel


class TopicModel(NamedDateTimeModel):
    forum = models.ForeignKey('forum.ForumModel', on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=225)
    content = models.TextField()


    class Meta:
        verbose_name = 'Sujet'
        verbose_name_plural = 'Sujets'

    def __str__(self):
        return self.title