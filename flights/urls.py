from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()

router.register(
    'flights',
    views.FlightViewSets,
    basename='flight'
)

urlpatterns = [
    path('', include(router.urls), name='flight')
]