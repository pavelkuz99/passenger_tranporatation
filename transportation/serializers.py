from rest_framework import serializers
from transportation.models import Route, Ride  # ClientRide, Vehicle, Driver, Client
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


class RideSerializer(serializers.HyperlinkedModelSerializer):
    route = serializers.SlugRelatedField(queryset=Route.objects.all(), slug_field='start_end')

    class Meta:
        model = Ride
        fields = (
            'url',
            'pk',
            'route',
            'date_and_time',
            # 'driver',
            # 'vehicle',
            # 'clients'
        )

# # ok
# class DriverSerializer(serializers.HyperlinkedModelSerializer):
#     rides = serializers.HyperlinkedRelatedField(
#         many=True,
#         read_only=True,
#         view_name='ride-detail'
#     )
#
#     class Meta:
#         model = Driver
#         fields = (
#             'url',
#             'pk',
#             'name',
#             'phone',
#             'rating',
#             'rides'
#         )
#
#
# # ok
# class VehicleSerializer(serializers.HyperlinkedModelSerializer):
#     rides = serializers.HyperlinkedRelatedField(
#         many=True,
#         read_only=True,
#         view_name='ride-detail'
#     )
#
#     class Meta:
#         model = Vehicle
#         fields = (
#             'url',
#             'pk',
#             'model',
#             'color',
#             'license',
#             'rides'
#         )
#
#
# # ok
# class ClientSerializer(serializers.HyperlinkedModelSerializer):
#     rides = serializers.HyperlinkedRelatedField(
#         many=True,
#         read_only=True,
#         view_name='ride-detail'
#     )
#
#     class Meta:
#         model = Client
#         fields = (
#             'url',
#             'pk',
#             'name',
#             'phone',
#             'status',
#             'rides'
#         )






