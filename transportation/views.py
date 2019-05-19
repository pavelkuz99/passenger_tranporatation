from transportation.models import Route, Ride, Driver, Vehicle, Client, ClientOrder
from transportation.serializers import RouteSerializer, RideSerializer, DriverSerializer, VehicleSerializer, \
    ClientSerializer, ClientOrderSerializer
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


# CLIENT
class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-list'


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-detail'


# CLIENT_ORDERS
class ClientOrderList(generics.ListCreateAPIView):
    queryset = ClientOrder.objects.all()
    serializer_class = ClientOrderSerializer
    name = 'clientorder-list'


class ClientOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClientOrder.objects.all()
    serializer_class = ClientOrderSerializer
    name = 'clientorder-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'routes': reverse(RouteList.name, request=request),
            'rides': reverse(RideList.name, request=request),
            'drivers': reverse(DriverList.name, request=request),
            'vehicles': reverse(VehicleList.name, request=request),
            'clients': reverse(VehicleList.name, request=request),
        })