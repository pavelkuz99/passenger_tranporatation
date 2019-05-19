from django.db import models


class Route(models.Model):
    start_end = models.CharField(max_length=30, blank=False, default='', unique=True)
    distance = models.IntegerField(default=0, blank=False)

    class Meta:
        ordering = ('start_end',)

    def __str__(self):
        return f'{self.start_end}: {self.distance}'


class Driver(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    driver_phone = models.CharField(max_length=13, blank=False, default='', unique=True)
    rating = models.IntegerField(default=0, blank=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}: {self.driver_phone}'


class Vehicle(models.Model):
    car_license = models.CharField(max_length=7, blank=False, default='', unique=True)
    car_model = models.CharField(max_length=15, blank=False, default='')
    color = models.CharField(max_length=15, blank=False, default='white')

    class Meta:
        ordering = ('car_license',)

    def __str__(self):
        return f'{self.car_license}:{self.car_model}:{self.color}'


class Ride(models.Model):
    start_end = models.CharField(max_length=30, blank=False, default='')
    date_and_time = models.DateTimeField()
    driver_phone = models.CharField(max_length=13, blank=False, default='')
    car_license = models.CharField(max_length=7, blank=False, default='')
    route = models.ForeignKey(
        Route,
        related_name='rides',
        on_delete=models.CASCADE
    )
    driver = models.ForeignKey(
        Driver,
        related_name='rides',
        on_delete=models.CASCADE
    )
    vehicle = models.ForeignKey(
        Vehicle,
        related_name='rides',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('date_and_time',)

    def __str__(self):
        return f'{self.route}: {self.date_and_time}'


class Client(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    phone = models.CharField(max_length=13, blank=False, default='', unique=True)
    status = models.CharField(max_length=15, blank=False, default='normal')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}: {self.phone}: {self.status}'


class ClientOrder(models.Model):
    client = models.ForeignKey(
        Client,
        related_name='orders',
        on_delete=models.CASCADE
    )
    ride = models.ForeignKey(
        Ride,
        related_name='orders',
        on_delete=models.CASCADE,
    )

