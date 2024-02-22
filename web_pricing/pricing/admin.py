from django.contrib import admin

from .models import Результат_Шкафы_с_артикулами


class Результат_Шкафы_с_артикуламиAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Результат_Шкафы_с_артикулами._meta.fields]

    def preview(self, obj):
        return obj.links.name
    
    def public_url(self, obj):
        return obj.links.name
    
    def file(self, obj):
        return obj.links.name


admin.site.register(Результат_Шкафы_с_артикулами, Результат_Шкафы_с_артикуламиAdmin)

