"""Markers API URL Configuration."""

from rest_framework import routers
router = routers.DefaultRouter()
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import ToponymViewSet
router.register(r"toponyms", ToponymViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import LineToponymViewSet
router.register(r"linetoponym", LineToponymViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import MonumentViewSet
router.register(r"monuments", MonumentViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import MunicipalViewSet
router.register(r"municipals", MunicipalViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import RegimentViewSet
router.register(r"regiments", RegimentViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import BattleViewSet
router.register(r"battles", BattleViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import RouteViewSet
router.register(r"routes", RouteViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import FortViewSet
router.register(r"forts", FortViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import CitiesViewSet
router.register(r"city", CitiesViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import UezdViewSet
router.register(r"uezds", UezdViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import UfaAreaViewSet
router.register(r"ufaarea", UfaAreaViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import DistrictsViewSet
router.register(r"districts", DistrictsViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import MemorialComplexViewSet
router.register(r"memorialcomplex", MemorialComplexViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import EternalFlameViewSet
router.register(r"eternalflame", EternalFlameViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import BustViewSet
router.register(r"bust", BustViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import Steles_oViewSet
router.register(r"steles_o", Steles_oViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import Monument_sViewSet
router.register(r"monument_s", Monument_sViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import GraffitiViewSet
router.register(r"graffiti", GraffitiViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import ReliefViewSet
router.register(r"relief", ReliefViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import CsignViewSet
router.register(r"csign", CsignViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
urlpatterns = router.urls