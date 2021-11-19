from django.db import models
#from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=200)
    postcode = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Address(models.Model):
    apartment_number = models.IntegerField(null=True, blank=True)
    building_number = models.IntegerField(default=0)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city')

    def __str__(self):
        return str(self.city.name) + " " + str(self.apartment_number) + "/" + str(self.building_number)


class Personal_Data(models.Model):
    name = models.CharField(max_length=200)
    nip = models.CharField(max_length=200, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='address')

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200)
    unit_price = models.DecimalField(decimal_places=2, max_digits=10)
    tax_rate = models.DecimalField(decimal_places=2, max_digits=2)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    number = models.CharField(max_length=200)
    date_of_issue = models.DateField('date of issue')
    date_of_delivery = models.DateField('date of delivery')
    date_of_payment = models.DateField('date of payment')
    seller = models.ForeignKey(Personal_Data, on_delete=models.CASCADE, related_name='seller')
    buyer = models.ForeignKey(Personal_Data, on_delete=models.CASCADE, related_name='buyer')

    def __str__(self):
        return self.number


class Service_Invoice(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='friendlistOwner')
    quantity = models.IntegerField(default=0)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='friend')

    def __str__(self):
        return self.service.name + " times " + str(self.quantity) + " for " + self.invoice.number


