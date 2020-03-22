"""
ViewsSets for the Event service API API
"""
from .models import City, Event, Participant, Rating
from .serializers import CitySerializer, EventSerializer, EventActionSerializer, ParticipantSerializer, RatingSerializer
from rest_framework import viewsets
import django_filters


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventActionSerializer
    # To allow filtering based on city or date
    filterset_fields = ('city', 'date') 


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer