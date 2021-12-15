from django import forms
from .models import *


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'postcode']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['apartment_number', 'building_number', 'city']


class Personal_DataForm(forms.ModelForm):
    class Meta:
        model = Personal_Data
        fields = ['name', 'nip']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'unit_price', 'tax_rate']


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['number', 'date_of_issue', 'date_of_delivery', 'date_of_payment', 'seller', 'buyer']


class Service_InvoiceForm(forms.ModelForm):
    class Meta:
        model = Service_Invoice
        fields = ['service', 'quantity']


class UploadFileForm(forms.Form):
    file = forms.FileField()

