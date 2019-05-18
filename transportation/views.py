from transportation.models import Route, Ride, Driver, Vehicle
from transportation.serializers import RouteSerializer, RideSerializer, DriverSerializer, VehicleSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse


# ROUTE
class RouteList(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    name = 'route-list'


class RouteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    name = 'route-detail'


# RIDE
class RideList(generics.ListCreateAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    name = 'ride-list'


class RideDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    name = 'ride-detail'


# DRIVER
class DriverList(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    name = 'driver-list'


class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    name = 'driver-detail'


# VEHICLE
class VehicleList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    name = 'vehicle-list'


class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    name = 'vehicle-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'routes': reverse(RouteList.name, request=request),
            'rides': reverse(RideList.name, request=request),
            'drivers': reverse(DriverList.name, request=request),
            # 'users': reverse(UserList.name, request=request),
        })