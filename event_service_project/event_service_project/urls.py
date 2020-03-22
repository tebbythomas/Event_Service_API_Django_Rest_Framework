from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from event_service_app import views

# Router is used to register viewsets
router = DefaultRouter()
router.register(r'city', views.CityViewSet)
router.register(r'users', views.ParticipantViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'ratings', views.RatingViewSet)


# The API URLs are determined automatically by the router
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]