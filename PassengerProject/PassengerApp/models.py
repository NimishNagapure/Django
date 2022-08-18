from django.db import models

# Create your models here.
class Passenger(models.Model):
    id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    travelpoint = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.fname + self.lname+self.travelpoint
