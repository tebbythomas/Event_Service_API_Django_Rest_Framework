from django.db import models
from django.urls import reverse_lazy
from datetime import datetime, timedelta
from django.core.validators import MaxValueValidator, MinValueValidator
from .constants import MIN_RATING_VAL, MAX_RATING_VAL, DEFAULT_RATING_VAL


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Participant(models.Model):
    # Full name used in case multiple people have the same first name
    full_name = models.CharField(max_length=100, unique=True)
    # City can be blank
    city = models.ForeignKey('City', models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.full_name


class Event(models.Model):
    # Event name must be unique
    name = models.CharField(max_length=100, unique=True)
    city = models.ForeignKey('City', models.DO_NOTHING, null=True, blank=True)
    # By default date of the event is set to 1 week from now
    date = models.DateTimeField(default=datetime.now()+timedelta(days=7))

    # Function to get number of people interested / rated the event
    def get_participant_count(self, name):
        return Rating.objects.filter(event__name=name).count()
        
    # Function to get each event participant's id
    def get_participants(self, name):
        return Rating.objects.filter(event__name=name).values_list('participant_id',flat=True)
        
    # Function to get average rating given by all participants of the event
    def get_avg_rating(self, name):
        query_set = Rating.objects.filter(event__name=name)
        ratings = list()
        for q in query_set:
            # Only considering ratings not Null/None
            if q.rating is not None:
                ratings.append(q.rating)
        if len(ratings) == 0:
            return 0
        else:
            return round(sum(ratings)/len(ratings), 2)

    # Function to get average rating given by participants living in the same city as the event
    def get_city_avg_rating(self, event_obj):
        query_set = Rating.objects.filter(event__name=event_obj.name)
        ratings = list()
        for q in query_set:
            # Checking if city of participant and event are same
            if q.event.city == q.participant.city:
                ratings.append(q.rating)
        if len(ratings) == 0:
            return 0
        else:
            return round(sum(ratings)/len(ratings), 2)
        
    def __str__(self):
        return self.name


class Rating(models.Model):
    # Event and participants are compulsory fields
    event = models.ForeignKey('Event', models.DO_NOTHING, null=False, blank=False)
    participant = models.ForeignKey('Participant', models.DO_NOTHING, null=False, blank=False)
    # Default assumes participant is interested
    interested  = models.BooleanField(default=True)
    # Rating has to be within the range of allowed values
    rating = models.FloatField(default=DEFAULT_RATING_VAL, validators=[MinValueValidator(MIN_RATING_VAL), MaxValueValidator(MAX_RATING_VAL)])
    
    def __str__(self):
        # To help readability in the admin display
        return f"Participant: {self.participant}, Event: {self.event}"

    class Meta:
        unique_together = ('event', 'participant',)