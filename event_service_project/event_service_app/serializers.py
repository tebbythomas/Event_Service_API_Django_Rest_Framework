"""
Serializers for all models
"""

from rest_framework import serializers
from .models import Event, Participant, Rating, City
from action_serializer import ModelActionSerializer


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = (
            'id', 'name',
        )


class ParticipantSerializer(serializers.ModelSerializer):
    city = CitySerializer().Meta()

    class Meta:
        model = Participant
        fields = (
            'id', 'full_name', 'city',
        )


class EventSerializer(serializers.ModelSerializer):
    city = CitySerializer().Meta()
    '''
    # To get total number of interested participants
    participant_count = serializers.SerializerMethodField(read_only=True)
    # To get interested participant objects
    participants = serializers.SerializerMethodField(read_only=True)
    # To get average rating of all interested users
    avg_rating = serializers.SerializerMethodField(read_only=True)
    # To get average rating of all interested users living in the same city as the event
    city_avg_rating = serializers.SerializerMethodField(read_only=True)

    # Calling method in Events model
    @staticmethod
    def get_participant_count(obj):
        return obj.get_participant_count(obj.name)

    # Calling method in Events model
    @staticmethod
    def get_participants(obj):
        return obj.get_participants(obj.name)

    # Calling method in Events model
    @staticmethod
    def get_avg_rating(obj):
        return obj.get_avg_rating(obj.name)

    # Calling method in Events model
    @staticmethod
    def get_city_avg_rating(obj):
        return obj.get_city_avg_rating(obj)
    '''

    class Meta:
        model = Event
        fields = (
            'id', 'name', 'city', 'date'
        )
        '''
        fields = (
            'id', 'name', 'city', 'date', 'participant_count', 'participants', 'avg_rating', 'city_avg_rating'
        )
        '''


class EventActionSerializer(ModelActionSerializer):
    """
    Serializer for event Serializer calss that gives less fields for the list view compared to detail view
    """
    city = CitySerializer().Meta()
    # To get total number of interested participants
    participant_count = serializers.SerializerMethodField(read_only=True)
    # To get interested participant objects
    participants = serializers.SerializerMethodField(read_only=True)
    # To get average rating of all interested users
    avg_rating = serializers.SerializerMethodField(read_only=True)
    # To get average rating of all interested users living in the same city as the event
    city_avg_rating = serializers.SerializerMethodField(read_only=True)

    # Calling method in Events model
    @staticmethod
    def get_participant_count(obj):
        return obj.get_participant_count(obj.name)

    # Calling method in Events model
    @staticmethod
    def get_participants(obj):
        return obj.get_participants(obj.name)

    # Calling method in Events model
    @staticmethod
    def get_avg_rating(obj):
        return obj.get_avg_rating(obj.name)

    # Calling method in Events model
    @staticmethod
    def get_city_avg_rating(obj):
        return obj.get_city_avg_rating(obj)

    class Meta:
        model = Event
        fields = (
            'id', 'name', 'city', 'date', 'participant_count', 'participants', 'avg_rating', 'city_avg_rating'
        )
        # Less fields retrieved in list view
        action_fields = {"list": {"fields": (
            'id', 'name', 'city', 'date', 'participant_count', 'avg_rating')},
            "detail": {"fields": (
            'id', 'name', 'city', 'date', 'participants', 'avg_rating', 'city_avg_rating')}}
        

class RatingSerializer(serializers.ModelSerializer):
    event = EventSerializer().Meta()
    participant = ParticipantSerializer().Meta()

    class Meta:
        model = Rating
        fields = (
            'id', 'event', 'participant', 'rating'
        )
