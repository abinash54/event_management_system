from django.db import models


# Create your models here.
class Service_Company(models.Model):
    S_TYPES = (
        ('catering', 'Catering'),
        ('decoration', 'Decoration'),
        ('Photo and Videography', 'Photo and Videography'),
        ('VIP Transport', 'VIP Transport')
    )

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    service_type = models.CharField(max_length=50, choices=S_TYPES)
    address = models.CharField(max_length=100, null=True, blank=True)
    license_id = models.CharField(max_length=20)
    isApproved = models.BooleanField() #add default


    def __str__(self):
        return self.name
		



class Customer_Detail(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    number_of_events = models.IntegerField(default=0)

    def __str__(self):
        return self.name
		


class Venue(models.Model):
    
    name = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    cost = models.FloatField()
    isAvailable = models.BooleanField(default=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
		



class Event(models.Model):
    EVENT_TYPES = (
        ('marriage', 'marriage'),
        ('birthday', 'birthday'),
        ('techfest', 'techfest'),
        ('exhibition', 'exhibition'),
        ('seminar', 'seminar'),
        ('conference','conference')
    )

    S_TYPES = (
        ('Catering', 'Catering'),
        ('Decoration', 'Decoration'),
        ('Photo and Videography', 'Photo and Videography'),
        ('VIP Transport', 'VIP Transport')
    )

    event_type = models.CharField(max_length=50,choices=EVENT_TYPES)
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer_Detail, on_delete=models.DO_NOTHING)
    phone = models.CharField(max_length=12)
    totalServices = models.IntegerField(default=0)
    service_1 = models.CharField(max_length=60, choices=S_TYPES, default='Catering')
    service_2 = models.CharField(max_length=60, choices=S_TYPES, blank=True, null=True)
    service_3 = models.CharField(max_length=60, choices=S_TYPES, blank=True, null=True)
    service_4 = models.CharField(max_length=60, choices=S_TYPES, blank=True, null=True)
    numberOfVIPs = models.IntegerField(default=0)
    venue = models.ForeignKey(Venue, on_delete=models.DO_NOTHING)
    isApproved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.event_type) + str(self.date)


