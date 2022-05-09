import datetime
from django.contrib.auth.decorators import login_required
from django.http import *
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.views import generic
from django.core.files import File
from django.core.files.storage import FileSystemStorage

from .dataFromText1 import *
from .textRecognition import *
from .forms import *
from .generatePDF import generateInvoice
from .models import *


@login_required
def list0(request):
    invoice_list = Invoice.objects.all()
    template = loader.get_template('faktury/lista.html')
    context = {
        'invoice_list': invoice_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def list1(request):
    invoice_list = Invoice.objects.order_by('number')
    template = loader.get_template('faktury/lista.html')
    context = {
        'invoice_list': invoice_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def list2(request):
    invoice_list = Invoice.objects.order_by('date_of_issue')
    template = loader.get_template('faktury/lista.html')
    context = {
        'invoice_list': invoice_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def list3(request):
    invoice_list = Invoice.objects.order_by('date_of_delivery')
    template = loader.get_template('faktury/lista.html')
    context = {
        'invoice_list': invoice_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def list4(request):
    invoice_list = Invoice.objects.order_by('date_of_payment')
    template = loader.get_template('faktury/lista.html')
    context = {
        'invoice_list': invoice_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def list5(request):
    invoice_list = Invoice.objects.order_by('seller')
    template = loader.get_template('faktury/lista.html')
    context = {
        'invoice_list': invoice_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def list6(request):
    invoice_list = Invoice.objects.order_by('buyer')
    template = loader.get_template('faktury/lista.html')
    context = {
        'invoice_list': invoice_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def service_list(request):
    service_list = Service.objects.all()
    template = loader.get_template('faktury/listaproduktow.html')
    context = {
        'service_list': service_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def traders_list(request):
    data_list = Personal_Data.objects.all()
    template = loader.get_template('faktury/listakontrahentow.html')
    context = {
        'data_list': data_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def Invoice_display(request, invoice_id):
    if request.method == 'POST':
        generateInvoice(invoice_id)
        return redirect('faktury:lista')
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    service_invoice_list = Service_Invoice.objects.filter(invoice_id=invoice_id)
    totaltaxed = 0
    totaluntaxed = 0
    for service in service_invoice_list:
        service.untaxed = service.service.unit_price * service.quantity
        service.taxed = "{:.2f}".format(float(service.untaxed * (1 + service.service.tax_rate)))
        totaluntaxed += service.untaxed
        totaltaxed += float(service.taxed)
    return render(request, 'faktury/faktura.html', {'invoice': invoice, 'service_invoice_list': service_invoice_list,
                                                    'totaltaxed': totaltaxed, 'totaluntaxed': totaluntaxed})


@login_required
def City_form(request):
    form = CityForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('faktury:lista')
    return render(request, 'faktury/dodajmiasto.html', {'form': form})


@login_required
def Address_form(request):
    form = AddressForm(request.POST)
    if form.is_valid():
        address = form.save(commit=False)
        address.user = request.user
        address.save()
        return redirect('faktury:lista')
    return render(request, 'faktury/dodajadres.html', {'form': form})


@login_required
def Personal_Data_form(request):
    form = Personal_DataForm(request.POST, prefix='name')
    form1 = AddressForm(request.POST)
    form2 = CityForm(request.POST, prefix='city')
    if form.is_valid() and form1.is_valid() and form2.is_valid():
        address = form1.save(commit=False)
        city = form2.save(commit=False)
        city_list = City.objects.all()
        codes = list()
        for c in city_list:
            codes.append(c.postcode)
        if city.postcode in codes:
            for c in city_list:
                if city.postcode == c.postcode:
                    address.city = c
        else:
            city.save()
            address.city = city
        address.save()
        data = form.save(commit=False)
        data.address = address
        data.user = request.user
        data.save()
        return redirect('faktury:listakontrahentow')
    return render(request, 'faktury/dodajdane.html', {'form': form, 'form1': form1, 'form2': form2})


@login_required
def Service_form(request):
    form = ServiceForm(request.POST)
    if form.is_valid():
        service = form.save(commit=False)
        service.user = request.user
        service.save()
        return redirect('faktury:listaproduktow')
    return render(request, 'faktury/dodajusluge.html', {'form': form})


@login_required
def Invoice_form(request):
    form = InvoiceForm(request.POST)
    form1 = Service_InvoiceForm(request.POST)
    if form.is_valid() and form1.is_valid():
        invoice = form.save(commit=False)
        invoice.user = request.user
        invoice.save()
        service = form1.save(commit=False)
        service.invoice = invoice
        service.save()
        return redirect('faktury:lista')
    return render(request, 'faktury/dodajfakture.html', {'form': form, 'form1': form1})


@login_required
def Service_Invoice_form(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    form = Service_InvoiceForm(request.POST)
    if form.is_valid():
        service = form.save(commit=False)
        service.invoice = invoice
        service.save()
        return redirect('faktury:lista')
    return render(request, 'faktury/dodajuslugedofaktury.html', {'form': form})


@login_required
def Invoice_delete_form(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    if request.method == "POST":
        invoice.delete()
        return redirect('faktury:lista')
    return render(request, 'faktury/usunfakture.html', {'invoice': invoice})


@login_required
def Invoice_edit_form(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    service_invoice_list = Service_Invoice.objects.filter(invoice_id=invoice_id)
    data = {'number': invoice.number, 'date_of_issue': invoice.date_of_issue,
            'date_of_delivery': invoice.date_of_delivery, 'date_of_payment': invoice.date_of_payment,
            'seller': invoice.seller, 'buyer': invoice.buyer}
    form = InvoiceForm(initial=data)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, initial=data, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('faktury:lista')
    return render(request, 'faktury/edytujfakture.html', {'form': form, 'service_invoice_list': service_invoice_list})


@login_required
def Service_delete_form(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    if request.method == "POST":
        service.delete()
        return redirect('faktury:listaproduktow')
    return render(request, 'faktury/usunprodukt.html', {'service': service})


@login_required
def Service_edit_form(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    data = {'name': service.name, 'unit_price': service.unit_price, 'tax_rate': service.tax_rate}
    form = ServiceForm(initial=data)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('faktury:listaproduktow')
    return render(request, 'faktury/edytujprodukt.html', {'form': form})


@login_required
def Service_Invoice_delete_form(request, service_invoice_id):
    service_invoice = get_object_or_404(Service_Invoice, pk=service_invoice_id)
    if request.method == "POST":
        service_invoice.delete()
        return redirect('/edytujfakture/' + str(service_invoice.invoice.id))
    return render(request, 'faktury/usunproduktzfaktury.html', {'service_invoice': service_invoice})


@login_required
def Service_Invoice_edit_form(request, service_invoice_id):
    service_invoice = get_object_or_404(Service_Invoice, pk=service_invoice_id)
    data = {'service': service_invoice.service, 'quantity': service_invoice.quantity,
            'invoice': service_invoice.invoice}
    form = Service_InvoiceForm(initial=data)
    if request.method == "POST":
        form = Service_InvoiceForm(request.POST, instance=service_invoice)
        if form.is_valid():
            form.save()
            return redirect('/edytujfakture/' + str(service_invoice.invoice.id))
    return render(request, 'faktury/edytujproduktzfaktury.html', {'form': form})


@login_required
def Data_delete_form(request, personal_data_id):
    personal_data = get_object_or_404(Personal_Data, pk=personal_data_id)
    if request.method == "POST":
        personal_data.delete()
        return redirect('faktury:listakontrahentow')
    return render(request, 'faktury/ununkontrahenta.html', {'personal_data': personal_data})


@login_required
def Data_edit_form(request, personal_data_id):
    personal_data = get_object_or_404(Personal_Data, pk=personal_data_id)
    data_address = get_object_or_404(Address, pk=personal_data.address.id)
    data_city = get_object_or_404(City, pk=data_address.city.id)
    data = {'name': personal_data.name, 'nip': personal_data.nip, 'address': personal_data.address}
    data1 = {'streetname': data_address.streetname, 'apartment_number': data_address.apartment_number,
             'building_number': data_address.building_number, 'city': data_address.city}
    data2 = {'name': data_city.name, 'postcode': data_city.postcode}
    form = Personal_DataForm(initial=data, prefix='name')
    form1 = AddressForm(initial=data1)
    form2 = CityForm(initial=data2, prefix='city')
    if request.method == "POST":
        form = Personal_DataForm(request.POST, instance=personal_data, prefix='name')
        form1 = AddressForm(request.POST, instance=data_address)
        form2 = CityForm(request.POST, instance=data_city, prefix='city')
        if form.is_valid() and form1.is_valid() and form2.is_valid():
            address = form1.save(commit=False)
            city = form2.save(commit=False)
            city_list = City.objects.all()
            if city in city_list:
                for c in city_list:
                    if city.postcode == c.postcode:
                        address.city = c
            else:
                city.save()
                address.city = city
            address.save()
            data = form.save(commit=False)
            data.address = address
            data.save()
            return redirect('faktury:listakontrahentow')
    return render(request, 'faktury/edytujkontrahenta.html', {'form': form, 'form1': form1, 'form2': form2})


@login_required
def upload_with_image(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            folder = 'uploads/'
            fs = FileSystemStorage(location=folder)
            filename = fs.save(file.name, file)
            textRecognition(folder + filename)
            if filename[1] == '1':
                data = DatafromTextW1("text_result2.txt")
            elif filename[1] == '2':
                data = DatafromTextW2("text_result2.txt")
            else:
                data = DatafromTextW3("text_result2.txt")
            # wyłuskanie danych ze skanu
            seller_city = City.create(data[7], data[6])
            seller_city.save()
            seller_address = Address.create_no_ap_number(data[9], data[8], seller_city)
            seller_address.save()
            buyer_city = City.create(data[13], data[12])
            buyer_city.save()
            buyer_address = Address.create_no_ap_number(data[15], data[14], buyer_city)
            buyer_address.save()
            seller = Personal_Data.create(data[4], data[16], seller_address)
            seller.save()
            buyer = Personal_Data.create_no_nip(data[10], buyer_address)
            buyer.save()
            invoice = Invoice.create(data[0], data[2], data[2], data[3], seller, buyer)
            invoice.user = request.user
            invoice.save()
            #data19 = data[19].split(",", 1)
            #d19 = float(data19[0]) + float(data19[1])/100
            service1 = Service.create(data[17], data[19], data[20])
            service1.save()
            addservice1 = Service_Invoice.create(service1, data[18], invoice)
            addservice1.save()
            if data[21] != " ":
                #data23 = data[23].split(",", 1)
                #d23 = float(data23[0]) + float(data23[1]) / 100
                service2 = Service.create(data[21], data[23], data[24])
                service2.save()
                addservice2 = Service_Invoice.create(service2, data[22], invoice)
                addservice2.save()
            if data[25] != " ":
                #data27 = data[27].split(",", 1)
                #d27 = float(data27[0]) + float(data27[1]) / 100
                service3 = Service.create(data[25], data[27], data[28])
                service3.save()
                addservice3 = Service_Invoice.create(service3, data[26], invoice)
                addservice3.save()
            return redirect('faktury:lista')
    else:
        form = UploadFileForm(request.POST, request.FILES)
    return render(request, 'faktury/dodajskan.html', {'form': form})
