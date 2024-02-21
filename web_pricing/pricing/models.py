from django.db import models

from ya_disk.models import Ya_links


class Результат_Шкафы_с_артикулами(models.Model):
    код = models.AutoField(db_column='Код', primary_key=True, blank=True)
    серия = models.TextField(db_column='Серия', blank=True, null=True)
    тип_шкафа = models.TextField(db_column='Тип_шкафа', blank=True, null=True)
    вариант_исполнения_шкафа = models.TextField(db_column='Вариант_исполнения_шкафа', blank=True, null=True)
    наименование_шкафа_на_сайте = models.TextField(db_column='Наименование_шкафа_на_сайте', blank=True, null=True)
    компановка_корпуса = models.TextField(db_column='Компановка_корпуса', blank=True, null=True)
    ширина = models.IntegerField(db_column='Ширина', blank=True, null=True)
    высота = models.IntegerField(db_column='Высота', blank=True, null=True)
    глубина = models.IntegerField(db_column='Глубина', blank=True, null=True)
    цвет_профиля = models.TextField(db_column='Цвет_профиля', blank=True, null=True)
    название_рендера = models.TextField(db_column='Название_рендера', blank=True, null=True)
    артикул_шкафа = models.OneToOneField(Ya_links, to_field='name', on_delete=models.DO_NOTHING, db_constraint=False, related_name="wardropes", db_column="Артикул_шкафа", unique=True)
    дверь_1_секционность = models.TextField(db_column='Дверь_1_Секционность', blank=True, null=True)
    дверь_2_секционность = models.TextField(db_column='Дверь_2_Секционность', blank=True, null=True)
    дверь_3_секционность = models.TextField(db_column='Дверь_3_Секционность', blank=True, null=True)
    д1_сек1_материал = models.TextField(db_column='Д1_Сек1_Материал', blank=True, null=True)
    д1_сек2_материал = models.TextField(db_column='Д1_Сек2_Материал', blank=True, null=True)
    д1_сек3_материал = models.TextField(db_column='Д1_Сек3_Материал', blank=True, null=True)
    д1_сек4_материал = models.TextField(db_column='Д1_Сек4_Материал', blank=True, null=True)
    д2_сек1_материал = models.TextField(db_column='Д2_Сек1_Материал', blank=True, null=True)
    д2_сек2_материал = models.TextField(db_column='Д2_Сек2_Материал', blank=True, null=True)
    д2_сек3_материал = models.TextField(db_column='Д2_Сек3_Материал', blank=True, null=True)
    д2_сек4_материал = models.TextField(db_column='Д2_Сек4_Материал', blank=True, null=True)
    д3_сек1_материал = models.TextField(db_column='Д3_Сек1_Материал', blank=True, null=True)
    д3_сек2_материал = models.TextField(db_column='Д3_Сек2_Материал', blank=True, null=True)
    д3_сек3_материал = models.TextField(db_column='Д3_Сек3_Материал', blank=True, null=True)
    д3_сек4_материал = models.TextField(db_column='Д3_Сек4_Материал', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Результат_Шкафы_с_артикулами'

class Результат_Стоимость_шкафов_CSKU(models.Model):
    Код = models.AutoField(db_column='Код', primary_key=True, blank=True)
    CKU = models.CharField(max_length=255, null=True)
    Артикул = models.OneToOneField(Ya_links, to_field='name', on_delete=models.DO_NOTHING, db_constraint=False, related_name="wardropes_price", db_column="Артикул", unique=True)
    Серия = models.CharField(max_length=255, null=True)
    Тип_шкафа = models.CharField(max_length=255, null=True)
    Вариант_исполнения_шкафа = models.CharField(max_length=255, null=True)
    Ширина = models.IntegerField(null=True)
    Высота = models.IntegerField(null=True)
    Глубина = models.FloatField(null=True)
    Наименование_шкафа_на_сайте = models.CharField(max_length=255, null=True)
    Признак_ВИ_Шкафа = models.CharField(max_length=255, null=True)
    Компановка_корпуса = models.CharField(max_length=255, null=True)
    Цвет_профиля = models.CharField(max_length=255, null=True)
    Sum_База_РРЦ = models.FloatField(null=True, db_column='Sum-База_РРЦ')
    Sum_Сибирь_РРЦ = models.FloatField(null=True, db_column='Sum-Сибирь_РРЦ')
    Sum_База_ОПТ = models.FloatField(null=True, db_column='Sum-База_ОПТ')
    Sum_Сибирь_ОПТ = models.FloatField(null=True, db_column='Sum-Сибирь_ОПТ')
    Sum_Экспорт = models.FloatField(null=True, db_column='Sum-Экспорт')
    Sum_Новоцентр_ОПТ = models.FloatField(null=True, db_column='Sum-Новоцентр_ОПТ')
    Sum_Крым_ОПТ = models.FloatField(null=True, db_column='Sum-Крым_ОПТ')
    Дверь_1_секционность = models.CharField(max_length=255, null=True)
    Дверь_1_материал = models.CharField(max_length=255, null=True)
    Дверь_2_секционность = models.CharField(max_length=255, null=True)
    Дверь_2_материал = models.CharField(max_length=255, null=True)
    Дверь_3_секционность = models.CharField(max_length=255, null=True)
    Дверь_3_материал = models.CharField(max_length=255, null=True)

    class Meta:
        managed = False
        db_table = 'Результат_Стоимость_шкафов_CSKU'