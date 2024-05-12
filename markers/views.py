"""Markers view."""

from django.views.generic.base import TemplateView
from django.shortcuts import render
from markers.models import Bust
class MainPageView(TemplateView):
    """Markers map view."""
    template_name = "mainpage.html"

class MarkersMapView(TemplateView):
    """Markers map view."""
    template_name = "map.html"

class Vov1945MapView(TemplateView):
    """Markers map view."""
    template_name = "map1945.html"

class Vov1945ObjectsInfoView(TemplateView):
    """Markers map view."""
    template_name = "objectsinfo.html"
