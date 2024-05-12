"""Markers models."""

from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField

class Toponym(models.Model): #топонимы
    name = models.CharField(max_length=255, verbose_name='Название') #описывает имя объекта длиной 255
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431), verbose_name='Расположение')
    place = models.CharField(max_length=255,null=True, verbose_name='Место') #описывает местоположение
    description = models.TextField(max_length= 2000,null=True, verbose_name='Описание') #описание
    audio = models.CharField(max_length=2000,default="", verbose_name='Аудио') #ссылка на web страницу без https
    photo = models.CharField(max_length=2000,default="", verbose_name='Фотографии') #ссылка на web страницу без https
    video = models.CharField(max_length=2000,default="", verbose_name='Видео') #ссылка на web страницу без https
    municipals = models.ForeignKey('Municipal',null=True, on_delete=models.SET_NULL, verbose_name='Муниципальный район')
    amenity = models.CharField(max_length=255, default="Монумент", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="toponym", editable = False) #описывает имя объекта длиной 255
    def __str__(self):
        """Return string representation."""
        return self.name
    class Meta:
        verbose_name = 'Топоним'
        verbose_name_plural = 'Топонимы'
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class LineToponym(models.Model): #топонимы линии
    name = models.CharField(max_length=255, verbose_name='Название') #описывает имя объекта длиной 255
    location = models.MultiLineStringField(null=True, verbose_name='Расположение') #задает локацию
    description = models.TextField(max_length= 2000,null=True, verbose_name='Описание') #описание
    audio = models.CharField(max_length=2000,default="", verbose_name='Аудио') #ссылка на web страницу без https
    photo = models.CharField(max_length=2000,default="", verbose_name='Фотографии') #ссылка на web страницу без https
    video = models.CharField(max_length=2000,default="", verbose_name='Видео') #ссылка на web страницу без https
    toponyms = models.ForeignKey('Toponym',null=True, on_delete=models.SET_NULL, verbose_name='Аудио')
    municipals = models.ForeignKey('Municipal',null=True, on_delete=models.SET_NULL)
    amenity = models.CharField(max_length=255, default="Монумент", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="toponym", editable = False) #описывает имя объекта длиной 255
    class Meta:
        verbose_name = 'Линейный топоним'
        verbose_name_plural = 'Линейные топонимы'
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Monument(models.Model): #памятник
    name = models.CharField(max_length=255, verbose_name='Название') #описывает имя объекта длиной 255
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431), verbose_name='Расположение')
    description = models.TextField(max_length= 2000,null=True, verbose_name='Описание') #описание
    architect = models.CharField(max_length=255,null=True, verbose_name='Архитектор')
    year = models.CharField(max_length=255,null=True, verbose_name='Год')
    municipals = models.ForeignKey('Municipal',null=True, on_delete=models.SET_NULL, verbose_name='Муниципальный район') #задает внешний ключ Pamyatniki, при удалении из первичной таблицы, запись во вторичной принимает значение NULL
    amenity = models.CharField(max_length=255, default="Памятник", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="monument", editable = False) #описывает имя объекта длиной 255
    audio = models.CharField(max_length=2000,default="", verbose_name='Аудио') #ссылка на web страницу без https
    photo = models.CharField(max_length=2000,default="", verbose_name='Фотографии') #ссылка на web страницу без https
    video = models.CharField(max_length=2000,default="", verbose_name='Видео') #ссылка на web страницу без https
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Памятник'
        verbose_name_plural = 'Памятники'
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Municipal(models.Model): #муниципальные районы
    name = models.CharField(max_length=255, verbose_name='Название')
    mpoly = models.MultiPolygonField(verbose_name='Геометрия')
    amenity = models.CharField(max_length=255, default="Муниципальный район", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="Municipal", editable = False) #описывает имя объекта длиной 255
    area = models.IntegerField(null=True, verbose_name='Территория')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Муниципальный район'
        verbose_name_plural = 'Муниципальные районы'
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Regiment(models.Model): #полк
    name = models.CharField(max_length=255, verbose_name='Название')
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431), verbose_name='Расположение')
    period = models.TextField(max_length= 1000,null=True, verbose_name='Период существования') #период существования
    place = models.CharField(max_length= 255,null=True, verbose_name='Место формирования') #место формирования
    size = models.TextField(max_length= 1000,null=True, verbose_name='Численность') #численность
    commander = models.TextField(max_length= 500,null=True, verbose_name='Командир') #командир
    amenity = models.CharField(max_length=255, default="Полк", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="regiment", editable = False) #описывает имя объекта длиной 255
    audio = models.CharField(max_length=2000,default="", verbose_name='Аудио') #ссылка на web страницу без https
    photo = models.CharField(max_length=2000,default="", verbose_name='Фотографии') #ссылка на web страницу без https
    video = models.CharField(max_length=2000,default="", verbose_name='Видео') #ссылка на web страницу без https
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Полк'
        verbose_name_plural = 'Полки'
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Battle(models.Model): #сражения
    name = models.CharField(max_length=255, verbose_name='Название')
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431), verbose_name='Расположение')
    description = models.TextField(max_length= 2000,null=True, verbose_name='Описание') #описание
    year = models.DateField(null=True, verbose_name='Год')
    regiments = models.ForeignKey('Regiment',null=True, on_delete=models.SET_NULL, verbose_name='Полк')
    amenity = models.CharField(max_length=255, default="Сражение", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="battle", editable = False) #описывает имя объекта длиной 255
    audio = models.CharField(max_length=2000,default="", verbose_name='Аудио') #ссылка на web страницу без https
    photo = models.CharField(max_length=2000,default="", verbose_name='Фотографии') #ссылка на web страницу без https
    video = models.CharField(max_length=2000,default="", verbose_name='Видео') #ссылка на web страницу без https
    def __str__(self):
        return self.description
    class Meta:
        verbose_name = 'Сражение'
        verbose_name_plural = 'Сражения'
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Route(models.Model): #маршрут
    name = models.CharField(max_length=255, verbose_name='Название')
    location = models.MultiLineStringField(null=True, verbose_name='Расположение') #задает локацию
    length = models.CharField(max_length= 255,null=True, verbose_name='Протяженность') #протяженность
    duration = models.CharField(max_length= 255,null=True, verbose_name='Продолжительность') #продолжительность
    kuda = models.CharField(max_length= 255,null=True, verbose_name='Куда') #продолжительность
    otkuda = models.CharField(max_length= 255,null=True, verbose_name='Откуда') #продолжительность
    regiment = models.ForeignKey('Regiment',null=True, on_delete=models.SET_NULL, verbose_name='Полк')
    amenity = models.CharField(max_length=255, default="Маршрут", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="route", editable = False) #описывает имя объекта длиной 255
    audio = models.CharField(max_length=2000,default="", verbose_name='Аудио') #ссылка на web страницу без https
    photo = models.CharField(max_length=2000,default="", verbose_name='Фотографии') #ссылка на web страницу без https
    video = models.CharField(max_length=2000,default="", verbose_name='Видео') #ссылка на web страницу без https
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Fort(models.Model): #крепости
    name = models.CharField(max_length=255, verbose_name='Название')
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431), verbose_name='Расположение')
    latitude = models.CharField(max_length=255, null=True, editable = False) #описывает имя объекта длиной 255
    longitude = models.CharField(max_length=255, null=True, editable = False) #описывает имя объекта длиной 255
    description = models.TextField(max_length= 2000,null=True, verbose_name='Описание') #описание
    battles = models.ForeignKey('Battle',null=True, on_delete=models.SET_NULL, verbose_name='Сражения')
    amenity = models.CharField(max_length=255, default="Крепость", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="fort", editable = False) #описывает имя объекта длиной 255
    audio = models.CharField(max_length=2000,default="", verbose_name='Аудио') #ссылка на web страницу без https
    photo = models.CharField(max_length=2000,default="", verbose_name='Фотографии') #ссылка на web страницу без https
    video = models.CharField(max_length=2000,default="", verbose_name='Видео') #ссылка на web страницу без https
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Крепость'
        verbose_name_plural = 'Крепости'
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Cities(models.Model): #города
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431), verbose_name='Расположение')
    name = models.CharField(max_length=255, verbose_name='Название')
    amenity = models.CharField(max_length=255, default="Город", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="cities", editable = False) #описывает имя объекта длиной 255
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Uezd(models.Model): #уездные города
    name = models.CharField(max_length=255, verbose_name='Название')
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431), verbose_name='Расположение')
    description = models.TextField(blank=True, max_length= 2000,null=True, verbose_name='Описание') #описание
    audio = models.CharField(max_length=2000,default="", verbose_name='Аудио') #ссылка на web страницу без https
    photo = models.CharField(max_length=2000,default="", verbose_name='Фотографии') #ссылка на web страницу без https
    video = models.CharField(max_length=2000,default="", verbose_name='Видео') #ссылка на web страницу без https
    amenity = models.CharField(max_length=255, default="Уезд", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="uezd", editable = False) #описывает имя объекта длиной 255
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Уездный город'
        verbose_name_plural = 'Уездные города'
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Mesh1(models.Model): #маршрут
    location = models.MultiLineStringField(null=True, verbose_name='Расположение') #задает локацию
    polk = models.CharField(max_length=255, verbose_name='Полк')
    otkuda = models.CharField(blank=True,max_length= 255,null=True, verbose_name='Откуда') #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True, verbose_name='Куда') #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True, verbose_name='Продолжительность') #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True, verbose_name='Протяженность') #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Mesh2(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk1(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk2(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk3(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk4(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk5(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk6(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk7(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk8(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk9(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk10(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk11(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk12(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk13(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk14(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk15(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk16(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk17(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk18(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk19(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk20(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class UfaArea(models.Model): #территории
    name = models.CharField(max_length=255, verbose_name='Название')
    mpoly = models.MultiPolygonField(verbose_name='Геометрия')
    amenity = models.CharField(max_length=255, default="Территория Уфы", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="UfaArea", editable = False) #описывает имя объекта длиной 255
    area = models.IntegerField(blank=True, null=True, verbose_name='Территория')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Территория Уфы'
        verbose_name_plural = 'Территория'
class Districts(models.Model): #территории
    name = models.CharField(max_length=255, verbose_name='Название')
    mpoly = models.MultiPolygonField(verbose_name='Геометрия')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class MemorialComplex(models.Model): #мемориальные комплексы
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431), verbose_name='Расположение')
    name = models.CharField(max_length=255, verbose_name='Название')
    place = models.CharField(max_length=255,null=True, verbose_name='Место')
    date = models.CharField(max_length=255,null=True, verbose_name='Дата')
    author = models.CharField(max_length=255,null=True, verbose_name='Автор')
    description = models.TextField(null=True, verbose_name='Описание') #описание
    who_opened = models.TextField(null=True, verbose_name='Кто открывал')
    area_around = models.CharField(max_length=255,null=True, verbose_name='Территория вокруг')
    security_level = models.CharField(max_length=255,null=True, verbose_name='Уровень охраны')
    binding = models.TextField(null=True, verbose_name='Привязан к конкретной местности')
    districts = models.ForeignKey('Districts',null=True, on_delete=models.SET_NULL, verbose_name='Район')
    audio = models.CharField(blank=True, max_length=2000,default="", verbose_name='Аудио') #ссылка на web страницу без https
    photo = models.CharField(blank=True, max_length=2000,default="", verbose_name='Фотографии') #ссылка на web страницу без https
    video = models.CharField(blank=True, max_length=2000,default="", verbose_name='Видео') #ссылка на web страницу без https
    amenity = models.CharField(max_length=255, default="Мемориальный комплекс", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="memorial complex", editable = False) #описывает имя объекта длиной 255
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Мемориальный комплекс'
        verbose_name_plural = 'Мемориальные комплексы'
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class EternalFlame(models.Model): #вечные огни
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431), verbose_name='Расположение')
    name = models.CharField(max_length=255, verbose_name='Название')
    place = models.CharField(max_length=255,null=True, verbose_name='Место')
    date = models.CharField(max_length=255,null=True, verbose_name='Дата')
    author = models.CharField(max_length=255,null=True, verbose_name='Автор')
    description = models.TextField(null=True, verbose_name='Описание') #описание
    material = models.CharField(max_length=255,null=True, verbose_name='Материал')
    who_opened = models.TextField(null=True, verbose_name='Кто открывал')
    area_around = models.CharField(max_length=255,null=True, verbose_name='Территория вокруг')
    security_level = models.CharField(max_length=255,null=True, verbose_name='Уровень охраны')
    binding = models.TextField(null=True, verbose_name='Привязан к конкретной местности')
    districts = models.ForeignKey('Districts',null=True, on_delete=models.SET_NULL, verbose_name='Район')
    audio = models.CharField(blank=True, max_length=2000,default="", verbose_name='Аудио') #ссылка на web страницу без https
    photo = models.CharField(blank=True, max_length=2000,default="", verbose_name='Фотографии') #ссылка на web страницу без https
    video = models.CharField(blank=True, max_length=2000,default="", verbose_name='Видео') #ссылка на web страницу без https
    amenity = models.CharField(max_length=255, default="Вечный огонь", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="eternal flame", editable = False) #описывает имя объекта длиной 255
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Вечный огонь'
        verbose_name_plural = 'Вечные огни'
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Bust(models.Model): #бюсты
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431), verbose_name='Расположение')
    name = models.CharField(max_length=255, verbose_name='Название')
    place = models.CharField(max_length=255,null=True, verbose_name='Место')
    date = models.CharField(max_length=255,null=True, verbose_name='Дата')
    author = models.CharField(max_length=255,null=True, verbose_name='Автор')
    description = models.TextField(null=True, verbose_name='Описание') #описание
    material = models.CharField(max_length=255,null=True, verbose_name='Материал')
    who_opened = models.TextField(null=True, verbose_name='Кто открывал')
    area_around = models.CharField(max_length=255,null=True, verbose_name='Территория вокруг')
    security_level = models.CharField(max_length=255,null=True, verbose_name='Уровень охраны')
    binding = models.TextField(null=True, verbose_name='Привязан к конкретной местности')
    districts = models.ForeignKey('Districts',null=True, on_delete=models.SET_NULL, verbose_name='Район')
    audio = models.CharField(blank=True, max_length=2000,default="", verbose_name='Аудио') #ссылка на web страницу без https
    photo = models.CharField(blank=True, max_length=2000,default="", verbose_name='Фотографии') #ссылка на web страницу без https
    video = models.CharField(blank=True, max_length=2000,default="", verbose_name='Видео') #ссылка на web страницу без https
    amenity = models.CharField(max_length=255, default="Бюст", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="bust", editable = False) #описывает имя объекта длиной 255
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Бюст'
        verbose_name_plural = 'Бюсты'
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Steles_o(models.Model): #стелы и обелиски
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431), verbose_name='Расположение')
    name = models.CharField(max_length=255, verbose_name='Название')
    place = models.CharField(max_length=255,null=True, verbose_name='Место')
    date = models.CharField(max_length=255,null=True, verbose_name='Дата')
    author = models.CharField(max_length=255,null=True, verbose_name='Автор')
    description = models.TextField(null=True, verbose_name='Описание') #описание
    material = models.CharField(max_length=255,null=True, verbose_name='Материал')
    who_opened = models.TextField(null=True, verbose_name='Кто открывал')
    area_around = models.CharField(max_length=255,null=True, verbose_name='Территория вокруг')
    security_level = models.CharField(max_length=255,null=True, verbose_name='Уровень охраны')
    binding = models.TextField(null=True, verbose_name='Привязан к конкретной местности')
    districts = models.ForeignKey('Districts',null=True, on_delete=models.SET_NULL, verbose_name='Район')
    audio = models.CharField(blank=True, max_length=2000,default="", verbose_name='Аудио') #ссылка на web страницу без https
    photo = models.CharField(blank=True, max_length=2000,default="", verbose_name='Фотографии') #ссылка на web страницу без https
    video = models.CharField(blank=True, max_length=2000,default="", verbose_name='Видео') #ссылка на web страницу без https
    amenity = models.CharField(max_length=255, default="Рельеф", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="bas-relief", editable = False) #описывает имя объекта длиной 255
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Стела (обелиск)'
        verbose_name_plural = 'Стелы (обелиски)'
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Monument_s(models.Model): #памятники и скульптуры
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431), verbose_name='Расположение')
    name = models.CharField(max_length=255, verbose_name='Название')
    place = models.CharField(max_length=255,null=True, verbose_name='Место')
    date = models.CharField(max_length=255,null=True, verbose_name='Дата')
    author = models.CharField(max_length=255,null=True, verbose_name='Автор')
    description = models.TextField(null=True, verbose_name='Описание') #описание
    material = models.CharField(max_length=255,null=True, verbose_name='Материал')
    who_opened = models.TextField(null=True, verbose_name='Кто открывал')
    area_around = models.CharField(max_length=255,null=True, verbose_name='Территория вокруг')
    security_level = models.CharField(max_length=255,null=True, verbose_name='Уровень охраны')
    binding = models.TextField(null=True, verbose_name='Привязан к конкретной местности')
    districts = models.ForeignKey('Districts',null=True, on_delete=models.SET_NULL, verbose_name='Район')
    audio = models.CharField(blank=True, max_length=2000,default="", verbose_name='Аудио') #ссылка на web страницу без https
    photo = models.CharField(blank=True, max_length=2000,default="", verbose_name='Фотографии') #ссылка на web страницу без https
    video = models.CharField(blank=True, max_length=2000,default="", verbose_name='Видео') #ссылка на web страницу без https
    amenity = models.CharField(max_length=255, default="Рельеф", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="bas-relief", editable = False) #описывает имя объекта длиной 255
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Памятник (скульптура)'
        verbose_name_plural = 'Памятники (скульптуры)'
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Graffiti(models.Model): #граффити
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431), verbose_name='Расположение')
    name = models.CharField(max_length=255, verbose_name='Название')
    place = models.CharField(max_length=255,null=True, verbose_name='Место')
    date = models.CharField(max_length=255,null=True, verbose_name='Дата')
    author = models.CharField(max_length=255,null=True, verbose_name='Автор')
    description = models.TextField(null=True, verbose_name='Описание') #описание
    material = models.CharField(max_length=255,null=True, verbose_name='Материал')
    who_opened = models.TextField(null=True, verbose_name='Кто открывал')
    area_around = models.CharField(max_length=255,null=True, verbose_name='Территория вокруг')
    security_level = models.CharField(max_length=255,null=True, verbose_name='Уровень охраны')
    binding = models.TextField(null=True, verbose_name='Привязан к конкретной местности')
    districts = models.ForeignKey('Districts',null=True, on_delete=models.SET_NULL, verbose_name='Район')
    audio = models.CharField(blank=True, max_length=2000,default="", verbose_name='Аудио') #ссылка на web страницу без https
    photo = models.CharField(blank=True, max_length=2000,default="", verbose_name='Фотографии') #ссылка на web страницу без https
    video = models.CharField(blank=True, max_length=2000,default="", verbose_name='Видео') #ссылка на web страницу без https
    amenity = models.CharField(max_length=255, default="Рельеф", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="bas-relief", editable = False) #описывает имя объекта длиной 255
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Граффити'
        verbose_name_plural = 'Граффити'
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Relief(models.Model): #рельефы
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431), verbose_name='Расположение')
    name = models.CharField(max_length=255, verbose_name='Название')
    place = models.CharField(max_length=255,null=True, verbose_name='Место')
    date = models.CharField(max_length=255,null=True, verbose_name='Дата')
    author = models.CharField(max_length=255,null=True, verbose_name='Автор')
    description = models.TextField(null=True, verbose_name='Описание') #описание
    material = models.CharField(max_length=255,null=True, verbose_name='Материал')
    who_opened = models.TextField(null=True, verbose_name='Кто открывал')
    area_around = models.CharField(max_length=255,null=True, verbose_name='Территория вокруг')
    security_level = models.CharField(max_length=255,null=True, verbose_name='Уровень охраны')
    binding = models.TextField(null=True, verbose_name='Привязан к конкретной местности')
    districts = models.ForeignKey('Districts',null=True, on_delete=models.SET_NULL, verbose_name='Район')
    audio = models.CharField(blank=True, max_length=2000,default="", verbose_name='Аудио') #ссылка на web страницу без https
    photo = models.CharField(blank=True, max_length=2000,default="", verbose_name='Фотографии') #ссылка на web страницу без https
    video = models.CharField(blank=True, max_length=2000,default="", verbose_name='Видео') #ссылка на web страницу без https
    amenity = models.CharField(max_length=255, default="Рельеф", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="bas-relief", editable = False) #описывает имя объекта длиной 255
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Рельеф'
        verbose_name_plural = 'Рельефы'
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Csign(models.Model): #памятные знаки
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431), verbose_name='Расположение')
    name = models.CharField(max_length=255, verbose_name='Название')
    place = models.CharField(max_length=255,null=True, verbose_name='Место')
    date = models.CharField(max_length=255,null=True, verbose_name='Дата')
    author = models.CharField(max_length=255,null=True, verbose_name='Автор')
    description = models.TextField(null=True, verbose_name='Описание') #описание
    material = models.CharField(max_length=255,null=True, verbose_name='Материал')
    who_opened = models.TextField(null=True, verbose_name='Кто открывал')
    area_around = models.CharField(max_length=255,null=True, verbose_name='Территория вокруг')
    security_level = models.CharField(max_length=255,null=True, verbose_name='Уровень охраны')
    binding = models.TextField(null=True, verbose_name='Привязан к конкретной местности')
    districts = models.ForeignKey('Districts',null=True, on_delete=models.SET_NULL, verbose_name='Район')
    audio = models.CharField(blank=True, max_length=2000,default="", verbose_name='Аудио') #ссылка на web страницу без https
    photo = models.CharField(blank=True, max_length=2000,default="", verbose_name='Фотографии') #ссылка на web страницу без https
    video = models.CharField(blank=True, max_length=2000,default="", verbose_name='Видео') #ссылка на web страницу без https
    amenity = models.CharField(max_length=255, default="Рельеф", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="bas-relief", editable = False) #описывает имя объекта длиной 255
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Памятный знак'
        verbose_name_plural = 'Памятные знаки'