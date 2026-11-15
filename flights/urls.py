from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()
router2 = DefaultRouter()

router.register(
    'flights',
    views.FlightViewSets,
    basename='flight'
)
router.register(
    'passengers',
    views.PassengerViewSets,
    basename='passenger'
)

urlpatterns = [
    path('api/', include(router.urls), name='flight'),
]