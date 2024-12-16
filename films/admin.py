from django.contrib import admin
from .models import Country, Film, Person, Genre
from feedback.models import Feedback

admin.site.register(Film)
admin.site.register(Person)
admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(Feedback)