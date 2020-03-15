from django.db import models

# Create your models here.

CHOICE_ARRIVAL_DEPARTURE = [
    ("Arrival", "Arrival"),
    ("Departure", "Departure"),
]

CHOICE_DOMESTIC_INTERNATIONAL = [
    ("Domestic", "Domestic"),
    ("International", "International"),

    
]
class AirportManager(models.Manager):
    def create_air(self, j):
        air = self.create(primary_key = j['primary_key'],report_period = j['report_period'],terminal = j['terminal'], arrival_departure = j['arrival_departure'],
                        domestic_international = j['domestic_international'],passenger_count= j['passenger_count'] )
        # do something with the book
        return(air)
class AirportModel(models.Model):
    primary_key = models.IntegerField("primary_key",null = False,default=0)
    report_period = models.CharField("report_period",max_length = 100)
    terminal = models.CharField("terminal", max_length=100)
    arrival_departure = models.CharField("arrival_departure",max_length = 50,choices = CHOICE_ARRIVAL_DEPARTURE)
    domestic_international = models.CharField("domestic_international",max_length=50,choices = CHOICE_DOMESTIC_INTERNATIONAL)
    passenger_count =  models.IntegerField("passenger_count",blank=True, null=True)

    objects = AirportManager()


    def __str__(self):
        return self.terminal




