from django.db import models

from base.helpers.named_date_time_model import NamedDateTimeModel


class ForumModel(NamedDateTimeModel):

    description = models.TextField()


    class Meta:
        verbose_name = 'Forum'
        verbose_name_plural = 'Forums'

    def __str__(self):
        return self.name
