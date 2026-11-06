from django.urls import path

from .import views

urlpatterns = [

    path(
        'flights/', views.FlightViewSets.as_view({
            'get': 'list'}), name="flights"
    )
]