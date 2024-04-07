from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "hotel"


class Guest(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    guest_name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

    class Meta:
        db_table = "guest"


class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guest_list = models.ManyToManyField(Guest)

    @property
    def hotel_name(self):
        return self.hotel.name

    def __str__(self):
        return self.guest_name

    class Meta:
        db_table = "reservation"
