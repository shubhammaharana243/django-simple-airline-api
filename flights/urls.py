from django.urls import path
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()

urlpatterns = [

    path(
        'flights/', views.FlightViewSets.as_view({
            'get': 'list',
            'post': 'create',}), name="flights"
    ),
    path(
        'details/<int:pk>', views.FlightViewSets.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }),
    )
]