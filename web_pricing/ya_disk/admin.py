from django.contrib import admin
from django.utils.html import format_html
from .models import Ya_links


# class Ya_linksAdmin(admin.ModelAdmin):
#     list_display = (
#         'preview_display',
#         'наименование_шкафа_на_сайте',
#         'серия',
#         'тип_шкафа',
#         'вариант_исполнения_шкафа',
#         'компановка_корпуса',
#         'ширина',
#         'высота',
#         'глубина',
#         'цвет_профиля',
#         'название_рендера',
#         'дверь_1_секционность',
#         'дверь_2_секционность',
#         'дверь_3_секционность',
#         'д1_сек1_материал',
#         'д1_сек2_материал',
#         'д1_сек3_материал',
#         'д1_сек4_материал',
#         'д2_сек1_материал',
#         'д2_сек2_материал',
#         'д2_сек3_материал',
#         'д2_сек4_материал',
#         'д3_сек1_материал',
#         'д3_сек2_материал',
#         'д3_сек3_материал',
#         'д3_сек4_материал'
#     )
#     readonly_fields = ('preview_display',)
#     list_filter = (
#         'wardropes__серия',
#         'wardropes__тип_шкафа',
#         'wardropes__вариант_исполнения_шкафа',
#         'wardropes__компановка_корпуса',
#         'wardropes__ширина',
#         'wardropes__высота',
#         'wardropes__глубина',
#         'wardropes__цвет_профиля',
#         'wardropes__дверь_1_секционность',
#         'wardropes__дверь_2_секционность',
#         'wardropes__дверь_3_секционность',
#         'wardropes__д1_сек1_материал',
#         'wardropes__д1_сек2_материал',
#         'wardropes__д1_сек3_материал',
#         'wardropes__д1_сек4_материал',
#         'wardropes__д2_сек1_материал',
#         'wardropes__д2_сек2_материал',
#         'wardropes__д2_сек3_материал',
#         'wardropes__д2_сек4_материал',
#         'wardropes__д3_сек1_материал',
#         'wardropes__д3_сек2_материал',
#         'wardropes__д3_сек3_материал',
#         'wardropes__д3_сек4_материал',
#     )

#     def preview_display(self, obj):
#         if obj.preview:
#             return format_html('<img src="data:image/jpeg;base64,{}" style="max-height: 2000px; max-width: 2000px;" />', obj.preview)
#         else:
#             return '-'

#     preview_display.short_description = 'Preview'

#     def наименование_шкафа_на_сайте(self, obj):
#         return obj.wardropes.наименование_шкафа_на_сайте

#     def серия(self, obj):
#         return obj.wardropes.серия

#     def тип_шкафа(self, obj):
#         return obj.wardropes.тип_шкафа

#     def вариант_исполнения_шкафа(self, obj):
#         return obj.wardropes.вариант_исполнения_шкафа

#     def компановка_корпуса(self, obj):
#         return obj.wardropes.компановка_корпуса

#     def ширина(self, obj):
#         return obj.wardropes.ширина

#     def высота(self, obj):
#         return obj.wardropes.высота

#     def глубина(self, obj):
#         return obj.wardropes.глубина

#     def цвет_профиля(self, obj):
#         return obj.wardropes.цвет_профиля

#     def название_рендера(self, obj):
#         return obj.wardropes.название_рендера

#     def дверь_1_секционность(self, obj):
#         return obj.wardropes.дверь_1_секционность

#     def дверь_2_секционность(self, obj):
#         return obj.wardropes.дверь_2_секционность

#     def дверь_3_секционность(self, obj):
#         return obj.wardropes.дверь_3_секционность

#     def д1_сек1_материал(self, obj):
#         return obj.wardropes.д1_сек1_материал

#     def д1_сек2_материал(self, obj):
#         return obj.wardropes.д1_сек2_материал

#     def д1_сек3_материал(self, obj):
#         return obj.wardropes.д1_сек3_материал

#     def д1_сек4_материал(self, obj):
#         return obj.wardropes.д1_сек4_материал

#     def д2_сек1_материал(self, obj):
#         return obj.wardropes.д2_сек1_материал

#     def д2_сек2_материал(self, obj):
#         return obj.wardropes.д2_сек2_материал

#     def д2_сек3_материал(self, obj):
#         return obj.wardropes.д2_сек3_материал

#     def д2_сек4_материал(self, obj):
#         return obj.wardropes.д2_сек4_материал

#     def д3_сек1_материал(self, obj):
#         return obj.wardropes.д3_сек1_материал

#     def д3_сек2_материал(self, obj):
#         return obj.wardropes.д3_сек2_материал

#     def д3_сек3_материал(self, obj):
#         return obj.wardropes.д3_сек3_материал

#     def д3_сек4_материал(self, obj):
#         return obj.wardropes.д3_сек4_материал


# admin.site.register(Ya_links, Ya_linksAdmin)
