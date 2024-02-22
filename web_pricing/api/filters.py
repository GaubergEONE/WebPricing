import django_filters

from pricing.models import Результат_Шкафы_с_артикулами
from ya_disk.models import Ya_links



def filter_by_values(self, queryset, name, value):
    values = value.split(',')
    filter_kwargs = {f'{name}__in': values}
    return queryset.filter(**filter_kwargs)

class WardrobeFilter(django_filters.FilterSet):

    серия = django_filters.CharFilter(method='filter_by_values')
    тип_шкафа = django_filters.CharFilter(method='filter_by_values')
    вариант_исполнения_шкафа = django_filters.CharFilter(method='filter_by_values')
    наименование_шкафа_на_сайте = django_filters.CharFilter(method='filter_by_values')
    компановка_корпуса = django_filters.CharFilter(method='filter_by_values')
    ширина = django_filters.CharFilter(method='filter_by_values')
    высота = django_filters.CharFilter(method='filter_by_values')
    глубина = django_filters.CharFilter(method='filter_by_values')
    цвет_профиля = django_filters.CharFilter(method='filter_by_values')
    дверь_1_секционность = django_filters.CharFilter(method='filter_by_values')
    дверь_2_секционность = django_filters.CharFilter(method='filter_by_values')
    дверь_3_секционность = django_filters.CharFilter(method='filter_by_values')
    д1_сек1_материал = django_filters.CharFilter(method='filter_by_values')
    д1_сек2_материал = django_filters.CharFilter(method='filter_by_values')
    д1_сек3_материал = django_filters.CharFilter(method='filter_by_values')
    д1_сек4_материал = django_filters.CharFilter(method='filter_by_values')
    д2_сек1_материал = django_filters.CharFilter(method='filter_by_values')
    д2_сек2_материал = django_filters.CharFilter(method='filter_by_values')
    д2_сек3_материал = django_filters.CharFilter(method='filter_by_values')
    д2_сек4_материал = django_filters.CharFilter(method='filter_by_values')
    д3_сек1_материал = django_filters.CharFilter(method='filter_by_values')
    д3_сек2_материал = django_filters.CharFilter(method='filter_by_values')
    д3_сек3_материал = django_filters.CharFilter(method='filter_by_values')
    д3_сек4_материал = django_filters.CharFilter(method='filter_by_values')

    def filter_by_values(self, queryset, name, value):
        values = value.split(',')
        filter_kwargs = {f'{name}__in': values}
        return queryset.filter(**filter_kwargs)

    class Meta:
        model = Результат_Шкафы_с_артикулами
        fields = []
