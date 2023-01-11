from django.db import models


# Create your models here.
class Tags(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'tags'
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return f'{self.name}'
