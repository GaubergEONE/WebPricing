from django.db import models

from pricing.models import Результат_Шкафы_с_артикулами


class Ya_links(models.Model):
    preview = models.URLField(max_length=1000)
    public_url = models.URLField(max_length=200)
    name = models.CharField(max_length=300, unique=True)
    name = models.OneToOneField(Результат_Шкафы_с_артикулами, to_field='артикул_шкафа', on_delete=models.DO_NOTHING, db_constraint=False, related_name="links", db_column="name", unique=True)
    file = models.CharField(max_length=1000)
