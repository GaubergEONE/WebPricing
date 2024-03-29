from django.http import HttpResponse
from django.db import transaction
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from pricing.models import Результат_Шкафы_с_артикулами
from .paginators import PageLimitPaginator
from .filters import WardrobeFilter

from .serializers import (UniqueFieldValuesSerializer,
                          WardrobeSerializer,)
from ya_disk.ya_api import fetch_data_and_update_db


@transaction.atomic
def get_ya_links(request):
    if fetch_data_and_update_db():
        return HttpResponse("Ссылки на рендеры обновлены.")
    else:
        return HttpResponse("Не удалось обновить ссылки на рендеры.")


class WardrobesFiltersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Результат_Шкафы_с_артикулами.objects.all()
    serializer_class = UniqueFieldValuesSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = WardrobeFilter

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        unique_values = {}

        fields_to_process = [
            'серия',
            'тип_шкафа',
            'вариант_исполнения_шкафа',
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

        for field in fields_to_process:
            unique_values[field] = list(
                queryset.order_by().values_list(field, flat=True).distinct()
            )

        serializer = UniqueFieldValuesSerializer(unique_values)
        return Response(serializer.data)


class WardrobesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Результат_Шкафы_с_артикулами.objects.all().prefetch_related('links').prefetch_related('wardropes_price')
    serializer_class = WardrobeSerializer
    pagination_class = PageLimitPaginator
    filter_backends = (DjangoFilterBackend,)
    filterset_class = WardrobeFilter
