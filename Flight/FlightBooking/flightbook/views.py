from django.shortcuts import render
from flightbook.models import Flight , Passenger ,Reservation
from flightbook.serializers import FlightSerializers,PassengerSerializers,ReservationSeralizers
from rest_framework import viewsets


# Create your views here.

def find_flights(request):
    flights = Flight.objects.filter(departureCity = request.data['departureCity'],arrivalCity=request.data['arrivalCity'],)
class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializers

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializers

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSeralizers