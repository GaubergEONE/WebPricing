from django.db import models


class Ya_links(models.Model):
    preview = models.URLField(max_length=1000)
    public_url = models.URLField(max_length=200)
    name = models.CharField(max_length=300, unique=True)
    file = models.CharField(max_length=1000)
