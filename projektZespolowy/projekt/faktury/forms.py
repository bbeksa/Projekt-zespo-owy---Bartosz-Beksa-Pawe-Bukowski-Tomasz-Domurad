from django import forms
from .models import *


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('name', 'postcode')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'postcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postcode'})
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('apartment_number', 'building_number', 'streetname', 'city')

        widgets = {
            'apartment_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apartment number'}),
            'building_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Building number'}),
            'streetname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Streetname'}),
            'city': forms.Select(attrs={'class': 'form-control'})
        }


class Personal_DataForm(forms.ModelForm):
    class Meta:
        model = Personal_Data
        fields = ('name', 'nip', 'address')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'nip': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NIP'}),
            'address': forms.Select(attrs={'class': 'form-control'})
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('name', 'unit_price', 'tax_rate')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'unit_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unit price'}),
            'tax_rate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tax rate'})
        }


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('number', 'date_of_issue', 'date_of_delivery', 'date_of_payment', 'seller', 'buyer')

        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Number'}),
            'date_of_issue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date of issue'}),
            'date_of_delivery': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date of delivery'}),
            'date_of_payment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date of payment'}),
            'seller': forms.Select(attrs={'class': 'form-control'}),
            'buyer': forms.Select(attrs={'class': 'form-control'})
        }


class Service_InvoiceForm(forms.ModelForm):
    class Meta:
        model = Service_Invoice
        fields = ('service', 'quantity')

        widgets = {
            'service': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'})
        }


class UploadFileForm(forms.Form):
    file = forms.FileField()

