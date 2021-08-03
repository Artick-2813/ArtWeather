from django.db import models


class City(models.Model):
    name_city = models.CharField(max_length=30)

    def __srt__(self):
        return self.name_city
