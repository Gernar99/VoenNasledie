"""Markers urls."""

from django.urls import path
from markers import views

from markers.views import MainPageView, MarkersMapView, Vov1945MapView, Vov1945ObjectsInfoView

app_name = "markers"

urlpatterns = [
    path("otechestvennaya_voina_1812/", MarkersMapView.as_view(), name='MarkersView'),
    path("velikaya_otechestvennaya_voina_1945/", Vov1945MapView.as_view(), name='Vov1945View'),
    path("velikaya_otechestvennaya_voina_1945_objects_info/", Vov1945ObjectsInfoView.as_view(), name='Vov1945ObjectsInfoView'),
    path("", MainPageView.as_view(), name='MainPage')
]