from django.shortcuts import get_object_or_404, render, redirect
from django.http import *
from django.views import generic
from django.template import loader
from .forms import *
import datetime

from .models import *


def list(request):
    invoice_list = Invoice.objects.all()
    template = loader.get_template('faktury/lista.html')
    context = {
        'invoice_list': invoice_list,
    }
    return HttpResponse(template.render(context, request))


def service_list(request):
    service_list = Service.objects.all()
    template = loader.get_template('faktury/listaproduktow.html')
    context = {
        'service_list': service_list,
    }
    return HttpResponse(template.render(context, request))


def traders_list(request):
    data_list = Personal_Data.objects.all()
    template = loader.get_template('faktury/listakontrahentow.html')
    context = {
        'data_list': data_list,
    }
    return HttpResponse(template.render(context, request))


def Invoice_display(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    template = loader.get_template('faktury/faktura.html')
    context = {
        'invoice': invoice,
    }
    return HttpResponse(template.render(context, request))



def City_form(request):
    form = CityForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'faktury/dodajmiasto.html', {'form': form})


def Address_form(request):
    form = AddressForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'faktury/dodajadres.html', {'form': form})


def Personal_Data_form(request):
    form = Personal_DataForm(request.POST)
    form1 = AddressForm(request.POST)
    if form.is_valid() and form1.is_valid():
        address = form1.save()
        data = form.save(commit=False)
        data.address = address
        data.save()
    return render(request, 'faktury/dodajdane.html', {'form': form, 'form1': form1})


def Service_form(request):
    form = ServiceForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'faktury/dodajusluge.html', {'form': form})


def Invoice_form(request):
    form = InvoiceForm(request.POST)
    form1 = Service_InvoiceForm(request.POST)
    if form.is_valid() and form1.is_valid():
        invoice = form.save()
        service = form1.save(commit=False)
        service.invoice = invoice
        service.save()
    return render(request, 'faktury/dodajfakture.html', {'form': form, 'form1': form1})


def Service_Invoice_form(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    form = Service_InvoiceForm(request.POST)
    if form.is_valid():
        service = form.save(commit=False)
        service.invoice = invoice
        service.save()
    return render(request, 'faktury/dodajuslugedofaktury.html', {'form': form})


def Invoice_delete_form(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    if request.method == "POST":
        invoice.delete()
        return redirect('faktury:list')
    return render(request, 'faktury/usunfakture.html', {'invoice': invoice})


def Invoice_edit_form(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    form = InvoiceForm(request.POST, instance=invoice)
    if form.is_valid():
        form.save()
        return redirect('faktury:list')
    return render(request, 'faktury/edytujfakture.html', {'form': form})


def Service_delete_form(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    if request.method == "POST":
        service.delete()
        return redirect('faktury:listaproduktow')
    return render(request, 'faktury/usunprodukt.html', {'service': service})


def Service_edit_form(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    form = ServiceForm(request.POST, instance=service)
    if form.is_valid():
        form.save()
        return redirect('faktury:listaproduktow')
    return render(request, 'faktury/edytujprodukt.html', {'form': form})


def Data_delete_form(request, personal_data_id):
    personal_data = get_object_or_404(Personal_Data, pk=personal_data_id)
    if request.method == "POST":
        personal_data.delete()
        return redirect('faktury:list')
    return render(request, 'faktury/usunkontrahenta.html', {'personal_data': personal_data})


def Data_edit_form(request, personal_data_id):
    personal_data = get_object_or_404(Personal_Data, pk=personal_data_id)
    data_address = get_object_or_404(Address, pk=personal_data.address.id)
    form = Personal_DataForm(request.POST, instance=personal_data)
    form1 = AddressForm(request.POST, instance=data_address)
    if form.is_valid() and form1.is_valid():
        address = form1.save()
        data = form.save(commit=False)
        data.address = address
        data.save()
        return redirect('faktury:listakontrahentow')
    return render(request, 'faktury/edytujkontrahenta.html', {'form': form, 'form1': form1})


def upload_with_image(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['file']
            #wyłuskanie danych ze skanu
            seller_city = City.create("cityname", "postcode")
            seller_city.save()
            seller_address = Address.create(1, 2, seller_city)
            seller_address.save()
            buyer_city = City.create("cityname", "postcode")
            buyer_city.save()
            buyer_address = Address.create(3, 4, buyer_city)
            buyer_address.save()
            seller = Personal_Data.create("seller_name", "nip", seller_address)
            seller.save()
            buyer = Personal_Data.create_no_nip("buyer name", buyer_address)
            buyer.save()
            invoice = Invoice.create_with_image("01/12/2021", 2021-12-13, 2021-12-13, 2021-12-13, seller, buyer, image)
            invoice.save()
            service = Service.create("coś", 12, 0.23)
            service.save()
            addservice = Service_Invoice.create(service, 50, invoice)
            addservice.save()
            return HttpResponseRedirect('faktury:list')
    else:
        form = UploadFileForm()
    return render(request, 'faktury/dodajskan.html', {'form': form})
