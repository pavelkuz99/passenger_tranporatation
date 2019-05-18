from django.db import models


class Route(models.Model):
    start = models.CharField(max_length=15, blank=False, default='')
    end = models.CharField(max_length=15, blank=False, default='')
    distance = models.IntegerField(max_length=3, default=0)

    class Meta:
        ordering = ('start',)

    def __str__(self):
        return f'{self.start} -> {self.end}: {self.distance}'


class Ride(models.Model):
    start = models.CharField(max_length=15, blank=False, default='')
    end = models.CharField(max_length=15, blank=False, default='')
    date_and_time = models.DateTimeField()
    ride_route = models.ForeignKey(
        Route,
        related_name='rides',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('date_and_time',)

    def __str__(self):
        return f'{self.start} -> {self.end}: {self.date_and_time}'


class Client(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    phone = models.CharField(max_length=13, blank=False, default='', unique=True)
    status = models.CharField(max_length=15, blank=False, default='normal')
    client_rides = models.ForeignKey(
        Ride,
        related_name='rides',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}: {self.phone}'


class ClientRides(models.Model):
    client = models.ForeignKey(
        Client,
        related_name='rides',
        on_delete=models.CASCADE
    )
    ride = mode
