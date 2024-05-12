# Register your models here.
from django.contrib.gis import admin
from markers.models import Toponym


@admin.register(Toponym)
class ToponymAdmin(admin.GISModelAdmin):
    """Toponyms admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "location", "description", "photo","audio")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import LineToponym
@admin.register(LineToponym)
class LineToponymAdmin(admin.GISModelAdmin):
    """Toponyms admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "location", "description", "photo","audio")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Monument
@admin.register(Monument)
class MonumentAdmin(admin.GISModelAdmin):
    """Monuments admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "location", "description", "photo","audio")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class ToponymInline(admin.TabularInline):
    model = Toponym
class MonumentInline(admin.TabularInline):
    model = Monument
from markers.models import Municipal
@admin.register(Municipal)
class MunicipalAdmin(admin.GISModelAdmin):
    """Municipals admin."""
    inlines = [
        ToponymInline,
        MonumentInline,
    ]
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {  
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "area")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Battle
@admin.register(Battle)
class BattleAdmin(admin.GISModelAdmin):
    """Battle admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "location", "description", "year", "regiments")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class BattleInline(admin.TabularInline):
    model = Battle
from markers.models import Regiment
@admin.register(Regiment)
class RegimentAdmin(admin.GISModelAdmin):
    """Regiment admin."""
    inlines = [
        BattleInline,
    ]
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "location", "period", "place", "size", "commander")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Route
@admin.register(Route)
class RouteAdmin(admin.GISModelAdmin):

    """Route admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "location", "length", "duration", "regiment")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Fort
@admin.register(Fort)
class FortAdmin(admin.GISModelAdmin):
    """Fort admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "location", "description", "battles")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Cities
@admin.register(Cities)
class CitiesAdmin(admin.GISModelAdmin):
    """Cities admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "location")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Uezd
@admin.register(Uezd)
class UezdAdmin(admin.GISModelAdmin):
    """Uezd admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "description", "photo", "audio", "video", "amenity", "amenity1")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import UfaArea
@admin.register(UfaArea)
class UfaAreaAdmin(admin.GISModelAdmin):
    """UfaArea admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "amenity", "amenity1", "area")
from markers.models import Districts
@admin.register(Districts)
class DistrictsAdmin(admin.GISModelAdmin):
    """Districts admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name",)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import MemorialComplex
@admin.register(MemorialComplex)
class MemorialComplexAdmin(admin.GISModelAdmin):
    """MemorialComplex admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "place", "date", "author", "description", "who_opened", "area_around", "security_level", "binding", "photo", "video", "audio")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import EternalFlame
@admin.register(EternalFlame)
class EternalFlameAdmin(admin.GISModelAdmin):
    """EternalFlame admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "place", "date", "author", "description", "material", "who_opened", "area_around", "security_level", "binding", "photo", "video", "audio")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Bust
@admin.register(Bust)
class BustAdmin(admin.GISModelAdmin):
    """Bust admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "place", "date", "author", "description", "material", "who_opened", "area_around", "security_level", "binding", "photo", "video", "audio")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Steles_o
@admin.register(Steles_o)
class Steles_oAdmin(admin.GISModelAdmin):
    """Steles_o admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "place", "date", "author", "description", "material", "who_opened", "area_around", "security_level", "binding", "photo", "video", "audio")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Monument_s
@admin.register(Monument_s)
class Monument_sAdmin(admin.GISModelAdmin):
    """Monument_s admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "place", "date", "author", "description", "material", "who_opened", "area_around", "security_level", "binding", "photo", "video", "audio")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Graffiti
@admin.register(Graffiti)
class GraffitiAdmin(admin.GISModelAdmin):
    """Graffiti admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "place", "date", "author", "description", "material", "who_opened", "area_around", "security_level", "binding", "photo", "video", "audio")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Relief
@admin.register(Relief)
class ReliefAdmin(admin.GISModelAdmin):
    """Relief admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "place", "date", "author", "description", "material", "who_opened", "area_around", "security_level", "binding", "photo", "video", "audio")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Csign
@admin.register(Csign)
class CsignAdmin(admin.GISModelAdmin):
    """Csign admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "place", "date", "author", "description", "material", "who_opened", "area_around", "security_level", "binding", "photo", "video", "audio")
