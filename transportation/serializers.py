from rest_framework import serializers
from transportation.models import Route, Ride, Driver, \
    Vehicle, Client, ClientOrder
import transportation.views


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    rides = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='ride-detail'
    )

    class Meta:
        model = Route
        fields = (
            'url',
            'pk',
            'start_end',
            'rides'
        )


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    rides = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='ride-detail'
    )

    class Meta:
        model = Driver
        fields = (
            'url',
            'pk',
            'name',
            'driver_phone',
            'rating',
            'rides'
        )


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    rides = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='ride-detail'
    )

    class Meta:
        model = Vehicle
        fields = (
            'url',
            'pk',
            'car_model',
            'color',
            'car_license',
            'rides'
        )


class RideSerializer(serializers.HyperlinkedModelSerializer):
    route = serializers.SlugRelatedField(queryset=Route.objects.all(), slug_field='start_end')
    driver = serializers.SlugRelatedField(queryset=Driver.objects.all(), slug_field='driver_phone')
    vehicle = serializers.SlugRelatedField(queryset=Vehicle.objects.all(), slug_field='car_license')

    class Meta:
        model = Ride
        fields = (
            'url',
            'pk',
            'route',
            'date_and_time',
            'driver',
            'vehicle',
            'orders',
        )
        read_only_fields = (
            'orders',
        )
        extra_kwargs = {
            'orders': {'many': True}
        }


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    ride = RideSerializer()

    class Meta:
        model = ClientOrder
        fields = (
            'url',
            'pk',
            'ride'
        )


class ClientSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = (
            'url',
            'pk',
            'name',
            'phone',
            'status',
            'orders'
        )


class ClientOrderSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(queryset=Client.objects.all(),
                                          slug_field='id')
    ride = serializers.SlugRelatedField(queryset=Ride.objects.all(),
                                        slug_field='id')

    class Meta:
        model = ClientOrder
        fields = (
            'url',
            'pk',
            'client',
            'ride'
        )
