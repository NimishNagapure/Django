from rest_framework import serializers
from PassengerApp.models import Passenger

class  PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id','fname','lname','travelpoint']