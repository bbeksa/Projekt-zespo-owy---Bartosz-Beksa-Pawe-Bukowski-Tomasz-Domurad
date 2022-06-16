from django.test import TestCase

from .models import *


# Create your tests here.
class QuestionModelTests(TestCase):

    def test_create_city(self):
        city = City.create("Sopot", "81-833")
        self.assertQuerysetEqual([city.name, city.postcode], ["Sopot", "81-833"])

    def test_create_address(self):
        city = City.create("Sopot", "81-833")
        address = Address.create("2", "4", "Klonowa", city)
        self.assertQuerysetEqual(
            [address.city, address.streetname, address.building_number, address.apartment_number]
            , [city, "Klonowa", "4", "2"])

    def test_create_personal_data(self):
        city = City.create("Sopot", "81-833")
        address = Address.create("2", "4", "Klonowa", city)
        personal_data = Personal_Data.create("Firma Krzak sp. z.o.o.", "0123456789", address)
        self.assertQuerysetEqual(
            [personal_data.address, personal_data.name, personal_data.nip]
            , [address, "Firma Krzak sp. z.o.o.", "0123456789"])

    def test_create_service(self):
        service = Service.create("Jabłko", "2", "0.23")
        self.assertQuerysetEqual(
            [service.name, service.unit_price, service.tax_rate]
            , ["Jabłko", "2", "0.23"])

    def test_create_invoice(self):
        city_seller = City.create("Sopot", "81-833")
        address_seller = Address.create("2", "4", "Klonowa", city_seller)
        seller = Personal_Data.create("seller", "0123456789", address_seller)
        city_buyer = City.create("Warszawa", "01-001")
        address_buyer = Address.create("21", "37", "Prosta", city_buyer)
        buyer = Personal_Data.create("buyer", "9876543210", address_buyer)
        invoice = Invoice.create("FZ test", "16.04.2022", "16.04.2022", "16.04.2022", seller, buyer)
        self.assertQuerysetEqual(
            [invoice.seller, invoice.buyer, invoice.number
                , invoice.date_of_issue, invoice.date_of_payment, invoice.date_of_delivery]
            , [seller, buyer, "FZ test"
                , "16.04.2022", "16.04.2022", "16.04.2022"])

    def test_create_service_invoice(self):
        city_seller = City.create("Sopot", "81-833")
        address_seller = Address.create("2", "4", "Klonowa", city_seller)
        seller = Personal_Data.create("seller", "0123456789", address_seller)
        city_buyer = City.create("Warszawa", "01-001")
        address_buyer = Address.create("21", "37", "Prosta", city_buyer)
        buyer = Personal_Data.create("buyer", "9876543210", address_buyer)
        invoice = Invoice.create("FZ test", "16.04.2022", "16.04.2022", "16.04.2022", seller, buyer)
        service = Service.create("Jabłko", "2", "0.23")
        service_invoice = Service_Invoice.create(service, "1000", invoice)
        self.assertQuerysetEqual(
            [service_invoice.service, service_invoice.quantity, service_invoice.invoice]
            , [service, "1000", invoice])
