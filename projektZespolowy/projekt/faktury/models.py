from django.db import models
#from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=200)
    postcode = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name, postcode):
        city = cls(name=name, postcode=postcode)
        return city


class Address(models.Model):
    streetname = models.CharField(max_length=200)
    apartment_number = models.IntegerField(null=True, blank=True)
    building_number = models.IntegerField(default=0)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city')

    def __str__(self):
        return str(self.city.name) + " " + str(self.apartment_number) + "/" + str(self.building_number)

    @classmethod
    def create(cls, apartment_number, building_number, streetname, city):
        address = cls(apartment_number=apartment_number, building_number=building_number, streetname=streetname, city=city)
        return address

    @classmethod
    def create_no_ap_number(cls, building_number, streetname, city):
        address = cls(building_number=building_number, streetname=streetname, city=city)
        return address


class Personal_Data(models.Model):
    name = models.CharField(max_length=200)
    nip = models.CharField(max_length=200, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='address')

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name, nip, address):
        personal_data = cls(name=name, nip=nip, address=address)
        return personal_data

    @classmethod
    def create_no_nip(cls, name, address):
        personal_data = cls(name=name, address=address)
        return personal_data


class Service(models.Model):
    name = models.CharField(max_length=200)
    unit_price = models.DecimalField(decimal_places=2, max_digits=10)
    tax_rate = models.DecimalField(decimal_places=2, max_digits=2)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name, unit_price, tax_rate):
        service = cls(name=name, unit_price=unit_price, tax_rate=tax_rate)
        return service


class Invoice(models.Model):
    number = models.CharField(max_length=200)
    date_of_issue = models.DateField('date of issue')
    date_of_delivery = models.DateField('date of delivery')
    date_of_payment = models.DateField('date of payment')
    seller = models.ForeignKey(Personal_Data, on_delete=models.CASCADE, related_name='seller')
    buyer = models.ForeignKey(Personal_Data, on_delete=models.CASCADE, related_name='buyer')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.number

    @classmethod
    def create(cls, number, date_of_issue, date_of_delivery, date_of_payment, seller, buyer):
        invoice = cls(number=number, date_of_issue=date_of_issue, date_of_delivery=date_of_delivery, date_of_payment=date_of_payment, seller=seller, buyer=buyer)
        return invoice

    @classmethod
    def create_with_image(cls, number, date_of_issue, date_of_delivery, date_of_payment, seller, buyer, image):
        invoice = cls(number=number, date_of_issue=date_of_issue, date_of_delivery=date_of_delivery, date_of_payment=date_of_payment, seller=seller, buyer=buyer, image=image)
        return invoice


class Service_Invoice(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='friendlistOwner')
    quantity = models.IntegerField(default=0)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='friend')

    def __str__(self):
        return self.service.name + " times " + str(self.quantity) + " for " + self.invoice.number

    @classmethod
    def create(cls, service, quantity, invoice):
        service_invoice = cls(service=service, quantity=quantity, invoice=invoice)
        return service_invoice


