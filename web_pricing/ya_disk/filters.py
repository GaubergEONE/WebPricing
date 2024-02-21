import django_filters

from pricing.models import Результат_Шкафы_с_артикулами
from ya_disk.models import Ya_links


class WardrobeFilter(django_filters.FilterSet):
    class Meta:
        model = Результат_Шкафы_с_артикулами
        fields = [
            'серия',
            'тип_шкафа',
            'вариант_исполнения_шкафа',
            'наименование_шкафа_на_сайте',
            'компановка_корпуса',
            'ширина',
            'высота',
            'глубина',
            'цвет_профиля',
            'дверь_1_секционность',
            'дверь_2_секционность',
            'дверь_3_секционность',
            'д1_сек1_материал',
            'д1_сек2_материал',
            'д1_сек3_материал',
            'д1_сек4_материал',
            'д2_сек1_материал',
            'д2_сек2_материал',
            'д2_сек3_материал',
            'д2_сек4_материал',
            'д3_сек1_материал',
            'д3_сек2_материал',
            'д3_сек3_материал',
            'д3_сек4_материал'
        ]

class LinksFilter(django_filters.FilterSet):
    серия = django_filters.CharFilter(field_name='wardropes__серия', lookup_expr='icontains')
    тип_шкафа = django_filters.CharFilter(field_name='wardropes__тип_шкафа', lookup_expr='icontains')
    вариант_исполнения_шкафа = django_filters.CharFilter(field_name='wardropes__вариант_исполнения_шкафа', lookup_expr='icontains')
    наименование_шкафа_на_сайте = django_filters.CharFilter(field_name='wardropes__наименование_шкафа_на_сайте', lookup_expr='icontains')
    компановка_корпуса = django_filters.CharFilter(field_name='wardropes__компановка_корпуса', lookup_expr='icontains')
    ширина = django_filters.NumberFilter(field_name='wardropes__ширина', lookup_expr='exact')
    высота = django_filters.NumberFilter(field_name='wardropes__высота', lookup_expr='exact')
    глубина = django_filters.NumberFilter(field_name='wardropes__глубина', lookup_expr='exact')
    цвет_профиля = django_filters.CharFilter(field_name='wardropes__цвет_профиля', lookup_expr='icontains')
    дверь_1_секционность = django_filters.CharFilter(field_name='wardropes__дверь_1_секционность', lookup_expr='icontains')
    дверь_2_секционность = django_filters.CharFilter(field_name='wardropes__дверь_2_секционность', lookup_expr='icontains')
    дверь_3_секционность = django_filters.CharFilter(field_name='wardropes__дверь_3_секционность', lookup_expr='icontains')
    д1_сек1_материал = django_filters.CharFilter(field_name='wardropes__д1_сек1_материал', lookup_expr='icontains')
    д1_сек2_материал = django_filters.CharFilter(field_name='wardropes__д1_сек2_материал', lookup_expr='icontains')
    д1_сек3_материал = django_filters.CharFilter(field_name='wardropes__д1_сек3_материал', lookup_expr='icontains')
    д1_сек4_материал = django_filters.CharFilter(field_name='wardropes__д1_сек4_материал', lookup_expr='icontains')
    д2_сек1_материал = django_filters.CharFilter(field_name='wardropes__д2_сек1_материал', lookup_expr='icontains')
    д2_сек2_материал = django_filters.CharFilter(field_name='wardropes__д2_сек2_материал', lookup_expr='icontains')
    д2_сек3_материал = django_filters.CharFilter(field_name='wardropes__д2_сек3_материал', lookup_expr='icontains')
    д2_сек4_материал = django_filters.CharFilter(field_name='wardropes__д2_сек4_материал', lookup_expr='icontains')
    д3_сек1_материал = django_filters.CharFilter(field_name='wardropes__д3_сек1_материал', lookup_expr='icontains')
    д3_сек2_материал = django_filters.CharFilter(field_name='wardropes__д3_сек2_материал', lookup_expr='icontains')
    д3_сек3_материал = django_filters.CharFilter(field_name='wardropes__д3_сек3_материал', lookup_expr='icontains')
    д3_сек4_материал = django_filters.CharFilter(field_name='wardropes__д3_сек4_материал', lookup_expr='icontains')


    class Meta:
        model = Ya_links
        fields = []
