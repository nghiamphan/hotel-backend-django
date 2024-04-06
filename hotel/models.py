from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "hotel"
