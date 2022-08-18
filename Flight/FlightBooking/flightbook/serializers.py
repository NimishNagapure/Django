from django.db.models import fields
from rest_framework import serializers
from .models import Flight,Passenger,Reservation

class FlightSerializers(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

        
class PassengerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSeralizers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'