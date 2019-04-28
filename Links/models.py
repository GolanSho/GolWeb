from django.db import models


class Links(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=2038)

