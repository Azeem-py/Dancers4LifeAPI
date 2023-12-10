from knox import views as knox_views
from .views import *
from django.urls import path, include

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"dance-class", DanceClassView, basename="dance-class")
router.register(r"events", EventView, basename="events")
router.register(r"enroll", EnrollView, basename="enroll")
router.register(r"ticket", TicketView, basename="ticket")

urlpatterns = [
    path("", include(router.urls)),
    path("class-data/<int:card>", DanceClassView.as_view({"get": "class_data"})),
    path("class-data/", DanceClassView.as_view({"get": "class_data"})),
    path("event-data/<int:card>", EventView.as_view({"get": "event_data"})),
    path("event-data/", EventView.as_view({"get": "event_data"})),
]