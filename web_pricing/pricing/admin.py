from django.contrib import admin

from .models import Результат_Шкафы_с_артикулами


class Результат_Шкафы_с_артикуламиAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Результат_Шкафы_с_артикулами._meta.fields]


admin.site.register(Результат_Шкафы_с_артикулами, Результат_Шкафы_с_артикуламиAdmin)

