from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Hotel, Reservation
from .serializers import HotelSerializer, ReservationSerializer


@api_view(["GET", "POST"])
def get_hotels(request):
    if request.method == "GET":
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        if isinstance(request.data, list):  # Check if a list of objects is provided
            serializer = HotelSerializer(data=request.data, many=True)
        else:
            serializer = HotelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


@api_view(["GET", "POST"])
def get_reservations(request):
    if request.method == "GET":
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        print("Request data:", request.data)
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            reservation = serializer.save()
            return Response({"confirmation_number": reservation.id}, status=201)
        else:
            print("Error:", serializer.errors)
            return Response(serializer.errors, status=400)
