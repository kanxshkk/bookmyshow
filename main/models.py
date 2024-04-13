from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings 
from django.db.models import Sum

class User(AbstractUser):

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='custom_user_permissions',
    )

    def __str__(self):
        return self.username

class Movie(models.Model):
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField() 

    def __str__(self):
        return self.title

class ShowTiming(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    max_tickets = models.PositiveIntegerField(default=100) 

    def available_tickets(self):
        booked_tickets = Booking.objects.filter(show_timing=self).aggregate(total_tickets=Sum('num_tickets'))['total_tickets'] or 0

        available_tickets = self.max_tickets - booked_tickets
        return available_tickets

    def __str__(self):
        return f"{self.movie.title} - {self.date} - {self.time}"


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    show_timing = models.ForeignKey(ShowTiming, on_delete=models.CASCADE)
    num_tickets = models.PositiveIntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def total_cost(self):
        return self.show_timing.movie.ticket_price * self.num_tickets

    def __str__(self):
        return f"{self.user.username} - {self.show_timing.movie.title} - {self.show_timing.date} - {self.show_timing.time}"

