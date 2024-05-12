"""Markers serializers."""

from rest_framework_gis import serializers
from rest_framework import serializers as serial
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Toponym


class ToponymSerializer(serializers.GeoFeatureModelSerializer): # ТОПОНИМЫ
    """Toponym GeoJSON serializer."""
    class Meta:
        """Toponym serializer meta class."""

        fields = ("id", "name", "description", "amenity", "amenity1", "photo", "audio", "video", "place")
        geo_field = "location"
        model = Toponym
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import LineToponym

class LineToponymSerializer(serializers.GeoFeatureModelSerializer): # ТОПОНИМЫ ЛИНИИ
    """Toponymline GeoJSON serializer."""

    class Meta:
        """Toponymline serializer meta class."""

        fields = ("id", "name", "description", "amenity", "amenity1", "photo", "audio", "video")
        geo_field = "location"
        model = LineToponym        
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Monument

class MonumentSerializer(serializers.GeoFeatureModelSerializer): # ПАМЯТНИКИ
    """Monument GeoJSON serializer."""

    class Meta:
        """Monument serializer meta class."""

        fields = ("id", "name", "description", "architect", "year", "amenity", "amenity1", "photo", "audio", "video")
        geo_field = "location"
        model = Monument
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Municipal

class MunicipalSerializer(serializers.GeoFeatureModelSerializer): # Муниципальный районы
    """Municipal GeoJSON serializer."""
    toponym_set = serial.StringRelatedField(many=True)
    monument_set = serial.StringRelatedField(many=True)
    class Meta:
        """Municipal serializer meta class."""

        fields = ("id", "name", "area", "amenity", "amenity1", 'toponym_set', 'monument_set')
        geo_field = "mpoly"
        model = Municipal
        
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Regiment

class RegimentSerializer(serializers.GeoFeatureModelSerializer): # ПОЛКИ
    """Regiment GeoJSON serializer."""
    battle_set = serial.StringRelatedField(many=True)
    class Meta:
        """Regiment serializer meta class."""

        fields = ("id", "name", "period", "place", "size", "commander", "photo", "audio", "video", "amenity", "amenity1", "battle_set")
        geo_field = "location"
        model = Regiment
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Battle

class BattleSerializer(serializers.GeoFeatureModelSerializer): # Сражения
    """Battle GeoJSON serializer."""

    class Meta:
        """Battle serializer meta class."""

        fields = ("id", "name", "description", "year", "regiments", "photo", "audio", "video", "amenity", "amenity1")
        geo_field = "location"
        model = Battle
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Route

class RouteSerializer(serializers.GeoFeatureModelSerializer): # Маршруты
    """Route GeoJSON serializer."""

    class Meta:
        """Route serializer meta class."""

        fields = ("id", "name", "length", "duration", "regiment", "photo", "audio", "video", "amenity", "amenity1")
        geo_field = "location"
        model = Route
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Fort

class FortSerializer(serializers.GeoFeatureModelSerializer): # Крепости
    """Route GeoJSON serializer."""

    class Meta:
        """Fort serializer meta class."""

        fields = ("id", "name", "description", "battles", "photo", "audio", "video", "amenity", "amenity1", "longitude", "latitude")
        geo_field = "location"
        model = Fort
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Cities

class CitiesSerializer(serializers.GeoFeatureModelSerializer): # Города
    """Cities GeoJSON serializer."""

    class Meta:
        """Cities serializer meta class."""

        fields = ("id", "name", "amenity", "amenity1")
        geo_field = "location"
        model = Cities
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Uezd

class UezdSerializer(serializers.GeoFeatureModelSerializer): # Уезды
    """Uezd GeoJSON serializer."""

    class Meta:
        """Uezd serializer meta class."""

        fields = ("id", "name", "description", "photo", "audio", "video", "amenity", "amenity1")
        geo_field = "location"
        model = Uezd
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import UfaArea

class UfaAreaSerializer(serializers.GeoFeatureModelSerializer): # Территория города Уфы
    """UfaArea GeoJSON serializer."""

    class Meta:
        """UfaArea serializer meta class."""

        fields = ("id", "name", "area", "amenity", "amenity1")
        geo_field = "mpoly"
        model = UfaArea
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#

from markers.models import Districts

class DistrictsSerializer(serializers.GeoFeatureModelSerializer): # Территория города Уфы
    """Districts GeoJSON serializer."""
    memorialcomplex_set = serial.StringRelatedField(many=True)
    eternalflame_set = serial.StringRelatedField(many=True)
    bust_set = serial.StringRelatedField(many=True)
    steles_o_set = serial.StringRelatedField(many=True)
    monument_s_set = serial.StringRelatedField(many=True)
    graffiti_set = serial.StringRelatedField(many=True)
    relief_set = serial.StringRelatedField(many=True)
    csign_set = serial.StringRelatedField(many=True)
    class Meta:
        """Districts serializer meta class."""

        fields = ("id", "name", 'memorialcomplex_set', 'eternalflame_set', 'bust_set', 'steles_o_set', 'monument_s_set', 'graffiti_set', 'relief_set', 'csign_set')
        geo_field = "mpoly"
        model = Districts
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#

from markers.models import MemorialComplex

class MemorialComplexSerializer(serializers.GeoFeatureModelSerializer): # Мемориальные комплексы
    """MemorialComplex GeoJSON serializer."""

    class Meta:
        """MemorialComplex serializer meta class."""

        fields = ("id", "name", "place", "date", "author", "description", "who_opened", "area_around", "security_level", "binding", "photo", "video", "audio", "amenity", "amenity1")
        geo_field = "location"
        model = MemorialComplex
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import EternalFlame

class EternalFlameSerializer(serializers.GeoFeatureModelSerializer): # Рельефы
    """EternalFlame GeoJSON serializer."""

    class Meta:
        """EternalFlame serializer meta class."""

        fields = ("id", "name", "place", "date", "author", "description", "material", "who_opened", "area_around", "security_level", "binding", "photo", "video", "audio", "amenity", "amenity1")
        geo_field = "location"
        model = EternalFlame
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Bust

class BustSerializer(serializers.GeoFeatureModelSerializer): # Бюсты
    """Bust GeoJSON serializer."""

    class Meta:
        """Bust serializer meta class."""

        fields = ("id", "name", "place", "date", "author", "description", "material", "who_opened", "area_around", "security_level", "binding", "photo", "video", "audio", "amenity", "amenity1")
        geo_field = "location"
        model = Bust
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Steles_o

class Steles_oSerializer(serializers.GeoFeatureModelSerializer): # Стелы и обелиски
    """Steles_o GeoJSON serializer."""

    class Meta:
        """Steles_o serializer meta class."""

        fields = ("id", "name", "place", "date", "author", "description", "material", "who_opened", "area_around", "security_level", "binding", "photo", "video", "audio", "amenity", "amenity1")
        geo_field = "location"
        model = Steles_o
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Monument_s

class Monument_sSerializer(serializers.GeoFeatureModelSerializer): # Памятники и скульптуры
    """Monument_s GeoJSON serializer."""

    class Meta:
        """Monument_s serializer meta class."""

        fields = ("id", "name", "place", "date", "author", "description", "material", "who_opened", "area_around", "security_level", "binding", "photo", "video", "audio", "amenity", "amenity1")
        geo_field = "location"
        model = Monument_s
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Graffiti

class GraffitiSerializer(serializers.GeoFeatureModelSerializer): # Памятники и скульптуры
    """Graffiti GeoJSON serializer."""

    class Meta:
        """Graffiti serializer meta class."""

        fields = ("id", "name", "place", "date", "author", "description", "material", "who_opened", "area_around", "security_level", "binding", "photo", "video", "audio", "amenity", "amenity1")
        geo_field = "location"
        model = Graffiti
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Relief

class ReliefSerializer(serializers.GeoFeatureModelSerializer): # Рельефы
    """Relief GeoJSON serializer."""

    class Meta:
        """Relief serializer meta class."""

        fields = ("id", "name", "place", "date", "author", "description", "material", "who_opened", "area_around", "security_level", "binding", "photo", "video", "audio", "amenity", "amenity1")
        geo_field = "location"
        model = Relief
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Csign

class CsignSerializer(serializers.GeoFeatureModelSerializer): # Памятные знаки
    """Csign GeoJSON serializer."""

    class Meta:
        """Csign serializer meta class."""

        fields = ("id", "name", "place", "date", "author", "description", "material", "who_opened", "area_around", "security_level", "binding", "photo", "video", "audio", "amenity", "amenity1")
        geo_field = "location"
        model = Csign
