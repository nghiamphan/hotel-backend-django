from rest_framework import serializers
from .models import Hotel, Guest, Reservation


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ["guest_name", "age", "gender"]


class ReservationSerializer(serializers.ModelSerializer):
    guest_list = GuestSerializer(many=True)

    class Meta:
        model = Reservation
        fields = ["hotel", "hotel_name", "check_in", "check_out", "guest_list"]

    def validate(self, data):
        if data["check_in"] > data["check_out"]:
            raise serializers.ValidationError("Check-out date must be later than check-in date.")
        return data

    def create(self, validated_data):
        guest_list_dict = validated_data.pop("guest_list")

        reservation = Reservation.objects.create(**validated_data)
        for guest_dict in guest_list_dict:
            guest = Guest.objects.create(**guest_dict)
            reservation.guest_list.add(guest)

        return reservation

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop("hotel")
        return rep
