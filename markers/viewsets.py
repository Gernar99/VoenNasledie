"""Markers API views."""
from rest_framework import viewsets
from rest_framework_gis import filters
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Toponym
from markers.serializers import ToponymSerializer


class ToponymViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Toponym.objects.all()
    serializer_class = ToponymSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import LineToponym
from markers.serializers import LineToponymSerializer


class LineToponymViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = LineToponym.objects.all()
    serializer_class = LineToponymSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Monument
from markers.serializers import MonumentSerializer


class MonumentViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Monument.objects.all()
    serializer_class = MonumentSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Municipal
from markers.serializers import MunicipalSerializer


class MunicipalViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Municipal.objects.all()
    serializer_class = MunicipalSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Regiment
from markers.serializers import RegimentSerializer


class RegimentViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Regiment.objects.all()
    serializer_class = RegimentSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Battle
from markers.serializers import BattleSerializer


class BattleViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#    
from markers.models import Route
from markers.serializers import RouteSerializer


class RouteViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Fort
from markers.serializers import FortSerializer


class FortViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Fort.objects.all()
    serializer_class = FortSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Cities
from markers.serializers import CitiesSerializer


class CitiesViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Uezd
from markers.serializers import UezdSerializer


class UezdViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Uezd.objects.all()
    serializer_class = UezdSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import UfaArea
from markers.serializers import UfaAreaSerializer


class UfaAreaViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = UfaArea.objects.all()
    serializer_class = UfaAreaSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Districts
from markers.serializers import DistrictsSerializer


class DistrictsViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Districts.objects.all()
    serializer_class = DistrictsSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import MemorialComplex
from markers.serializers import MemorialComplexSerializer


class MemorialComplexViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = MemorialComplex.objects.all()
    serializer_class = MemorialComplexSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import EternalFlame
from markers.serializers import EternalFlameSerializer


class EternalFlameViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = EternalFlame.objects.all()
    serializer_class = EternalFlameSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Bust
from markers.serializers import BustSerializer


class BustViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Bust.objects.all()
    serializer_class = BustSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Steles_o
from markers.serializers import Steles_oSerializer


class Steles_oViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Steles_o.objects.all()
    serializer_class = Steles_oSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Monument_s
from markers.serializers import Monument_sSerializer


class Monument_sViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Monument_s.objects.all()
    serializer_class = Monument_sSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Graffiti
from markers.serializers import GraffitiSerializer


class GraffitiViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Graffiti.objects.all()
    serializer_class = GraffitiSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Relief
from markers.serializers import ReliefSerializer


class ReliefViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Relief.objects.all()
    serializer_class = ReliefSerializer

#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Csign
from markers.serializers import CsignSerializer


class CsignViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Csign.objects.all()
    serializer_class = CsignSerializer