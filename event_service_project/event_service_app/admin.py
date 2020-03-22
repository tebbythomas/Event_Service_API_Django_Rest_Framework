from django.contrib import admin

from .models import Participant, Event, Rating, City

# Registering all our models with the admin
admin.site.register(Participant)
admin.site.register(Event)
admin.site.register(Rating)
admin.site.register(City)