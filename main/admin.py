# admin.py

from django.contrib import admin
from .models import Movie, ShowTiming, Booking,User

# Register your models here
admin.site.register(Movie)
admin.site.register(ShowTiming)
admin.site.register(Booking)
admin.site.register(User)