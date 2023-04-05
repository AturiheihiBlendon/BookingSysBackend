from django.db import models

# Create your models here


class Driver(models.Model):
    '''
    creates a driver table with buss details and route
    '''
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    bus_reg = models.CharField(max_length=200)
    no_of_seats = models.CharField(max_length=200)
    bus_type = models.CharField(max_length=200)
    route = models.CharField(max_length=500)

# creates table of bookings
# class Bookings(models.Model):
#     client_name = models.CharField(max_length=200)
#     client_surname = models.CharField(max_length=200)
#     bus_reg = models.CharField(max_length=200)
#     trip_time = models.CharField(max_length=200)
#     trip_date = models.CharField(max_length=200)
#     transaction_id = models.CharField(max_length=200)
#     trip_depature = models.CharField(max_length=500)
#     trip_destination = models.CharField(max_length=500)
