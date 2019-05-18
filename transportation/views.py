from transportation.models import Route, Ride
from transportation.serializers import RouteSerializer, RideSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse


class RouteList(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    name = 'route-list'


class RouteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    name = 'route-detail'


class RideList(generics.ListCreateAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    name = 'ride-list'


class RideDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    name = 'ride-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'routes': reverse(RouteList.name, request=request),
            'rides': reverse(RideList.name, request=request),
            # 'scores': reverse(PlayerScoreList.name, request=request),
            # 'users': reverse(UserList.name, request=request),
        })