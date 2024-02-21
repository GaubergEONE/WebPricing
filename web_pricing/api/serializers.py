from rest_framework import serializers

from pricing.models import Результат_Стоимость_шкафов_CSKU, Результат_Шкафы_с_артикулами

from ya_disk.models import Ya_links



class Ya_linksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ya_links
        fields = [
            'preview',
            'public_url',
            'name',
            'file',
        ]


class WardrobePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Результат_Стоимость_шкафов_CSKU
        fields = [
            'Sum_База_РРЦ', 'Sum_Сибирь_РРЦ', 'Sum_База_ОПТ',
            'Sum_Сибирь_ОПТ', 'Sum_Экспорт', 'Sum_Новоцентр_ОПТ',
            'Sum_Крым_ОПТ'
        ]


class WardrobeSerializer(serializers.ModelSerializer):
    links = Ya_linksSerializer(read_only=True)
    wardropes_price = WardrobePriceSerializer(read_only=True)

    class Meta:
        model = Результат_Шкафы_с_артикулами
        fields = [
            'wardropes_price',
            'links',
            'серия',
            'тип_шкафа',
            'вариант_исполнения_шкафа',
            'компановка_корпуса',
            'ширина',
            'высота',
            'глубина',
            'цвет_профиля',
            'название_рендера',
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
            'д3_сек4_материал',
        ]


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["door_1"] = {
            "секционность": representation.pop("дверь_1_секционность"),
            "сек1_материал": representation.pop("д1_сек1_материал"),
            "сек2_материал": representation.pop("д1_сек2_материал"),
            "сек3_материал": representation.pop("д1_сек3_материал"),
            "сек4_материал": representation.pop("д1_сек4_материал"),
        }
        representation["door_2"] = {
            "секционность": representation.pop("дверь_2_секционность"),
            "сек1_материал": representation.pop("д2_сек1_материал"),
            "сек2_материал": representation.pop("д2_сек2_материал"),
            "сек3_материал": representation.pop("д2_сек3_материал"),
            "сек4_материал": representation.pop("д2_сек4_материал"),
        }
        representation["door_3"] = {
            "секционность": representation.pop("дверь_3_секционность"),
            "сек1_материал": representation.pop("д3_сек1_материал"),
            "сек2_материал": representation.pop("д3_сек2_материал"),
            "сек3_материал": representation.pop("д3_сек3_материал"),
            "сек4_материал": representation.pop("д3_сек4_материал"),
        }
        
        representation.update(representation.pop("wardropes_price"))
        representation.update(representation.pop("links"))
        return representation







class UniqueFieldValuesSerializer(serializers.Serializer):

    class Meta:
        fields = [
            'серия',
            'тип_шкафа',
            'вариант_исполнения_шкафа',
            'компановка_корпуса',
            'ширина',
            'высота',
            'глубина',
            'цвет_профиля',
            'название_рендера',
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

    def to_representation(self, instance):
        return instance
