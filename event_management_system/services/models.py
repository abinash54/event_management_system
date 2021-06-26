
from django.db import models
from management.models import Service_Company

# Create your models here.

#service details
class Catering(models.Model):
    company = models.ForeignKey(Service_Company, on_delete=models.DO_NOTHING)

    food_item_1 = models.CharField(max_length=50)
    price_1 = models.DecimalField(max_digits=10, decimal_places=2)
    food_item_2 = models.CharField(max_length=50, null=True, blank=True)
    price_2 = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    food_item_3 = models.CharField(max_length=50, null=True, blank=True)
    price_3 = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    food_item_4 = models.CharField(max_length=50, null=True, blank=True)
    price_4 = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)

    license_number = models.CharField(max_length=50, null=True, blank=True)
    isApproved = models.BooleanField(default=False)

    class Meta:
        unique_together=['company', 'license_number']

    def __str__(self):
        return self.company.name


class Photo_n_Videography(models.Model):
    company = models.ForeignKey(Service_Company, on_delete=models.DO_NOTHING)
    no_of_equipments = models.IntegerField()
    charge = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.company.name


class VIP_Transport(models.Model):
    company = models.ForeignKey(Service_Company, on_delete=models.DO_NOTHING)

    no_of_vehicles = models.IntegerField()
    vehicle_1 = models.CharField(max_length=50)
    charge_1 = models.DecimalField(max_digits=10, decimal_places=2)
    vehicle_2 = models.CharField(max_length=50, null=True, blank=True)
    charge_2 = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    vehicle_3 = models.CharField(max_length=50, null=True, blank=True)
    charge_3 = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    vehicle_4 = models.CharField(max_length=50, null=True, blank=True)
    charge_4 = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.company.name


class Decoration(models.Model):
    company = models.ForeignKey(Service_Company, on_delete=models.DO_NOTHING)

    description = models.TextField()
    charge = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.company.name


