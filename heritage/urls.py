from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Homepage showing monasteries
    path("monastery/<int:monastery_id>/", views.monastery_detail, name="monastery_detail"),  # Monastery detail
    path("events/", views.events, name="events"),  # Upcoming events
]
