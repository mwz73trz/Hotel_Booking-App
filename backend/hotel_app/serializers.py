from django.db import models
from rest_framework import fields, serializers
from hotel_app.models import Guest, Hotel, Room, Booking

class GuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guest
        fields = ('name', 'age', 'phone', 'email')
        
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('name', 'location', 'phone', 'email')
        
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('room_no', 'price', 'hotel', 'is_booked') 
        
class BookingSerializer(serializers.ModelSerializer):
    guest = GuestSerializer
    hotel = HotelSerializer
    room = RoomSerializer
    class Meta:
        model = Booking
        fields = ('guest', 'hotel', 'room', 'checkin_date', 'checkout_date', 'charge')