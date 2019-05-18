from django.db import models


class Route(models.Model):
    start = models.CharField(max_length=15, blank=False, default='')
    end = models.CharField(max_length=15, blank=False, default='')
    distance = models.IntegerField(default=0)

    class Meta:
        ordering = ('start',)

    def __str__(self):
        return f'{self.start} -> {self.end}: {self.distance}'


class Ride(models.Model):
    start = models.CharField(max_length=15, blank=False, default='')
    end = models.CharField(max_length=15, blank=False, default='')
    date_and_time = models.DateTimeField()
    route = models.ForeignKey(
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
    ride = models.ForeignKey(
        Ride,
        related_name='clients',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}: {self.phone}'


class ClientRide(models.Model):
    client = models.ForeignKey(
        Client,
        related_name='rides',
        on_delete=models.CASCADE
    )
    ride = models.ForeignKey(
        Ride,
        on_delete=models.CASCADE
    )


class Driver(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    phone = models.CharField(max_length=13, blank=False, default='', unique=True)
    rating = models.IntegerField(blank=False, default=0)
    ride = models.ForeignKey(
        Ride,
        related_name='driver',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}: {self.phone}'


class Vehicle(models.Model):
    car_license = models.CharField(max_length=7, blank=False, default='')
    car_model = models.Model(max_length=15, blank=False, default='')
    color = models.CharField(max_length=15, blank=False, default='white')
    ride = models.ForeignKey(
        Ride,
        related_name='vehicle',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('car_license',)

    def __str__(self):
        return f'{self.car_license}:{self.car_model}:{self.color}'
