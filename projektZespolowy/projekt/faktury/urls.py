from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'faktury'
urlpatterns = [
    path('', views.list0, name='lista'),
    path('lista/1/', views.list1, name='lista1'),
    path('lista/2/', views.list2, name='lista2'),
    path('lista/3/', views.list3, name='lista3'),
    path('lista/4/', views.list4, name='lista4'),
    path('lista/5/', views.list5, name='lista5'),
    path('lista/6/', views.list6, name='lista6'),
    path('listakontrahentow/', views.traders_list, name='listakontrahentow'),
    path('listaproduktow/', views.service_list, name='listaproduktow'),
    path('dodajmiasto/', views.City_form, name='dodajmiasto'),
    path('dodajadres/', views.Address_form, name='dodajadres'),
    path('dodajdane/', views.Personal_Data_form, name='dodajdane'),
    path('dodajusluge/', views.Service_form, name='dodajusluge'),
    path('dodajfakture/', views.Invoice_form, name='dodajfakture'),
    path('dodajskan/', views.upload_with_image, name='dodajskan'),
    path('dodajskan/1', views.upload_with_image1, name='dodajskan1'),
    path('dodajskan/2', views.upload_with_image2, name='dodajskan2'),
    path('dodajskan/3', views.upload_with_image3, name='dodajskan3'),
    path('wybierzwzor/', views.Select_pattern, name='wybierzwzor'),
    path('faktura/<int:invoice_id>/', views.Invoice_display, name='faktura'),
    path('usunfakture/<int:invoice_id>/', views.Invoice_delete_form, name='usunfakture'),
    path('edytujfakture/<int:invoice_id>/', views.Invoice_edit_form, name='edytujfakture'),
    path('usunprodukt/<int:service_id>/', views.Service_delete_form, name='usunprodukt'),
    path('edytujprodukt/<int:service_id>/', views.Service_edit_form, name='edytujprodukt'),
    path('usunproduktzfaktury/<int:service_invoice_id>/', views.Service_Invoice_delete_form, name='usunproduktzfaktury'),
    path('edytujproduktzfaktury/<int:service_invoice_id>/', views.Service_Invoice_edit_form,
         name='edytujproduktzfaktury'),
    path('usunkontrahenta/<int:personal_data_id>/', views.Data_delete_form, name='usunkontrahenta'),
    path('edytujkontrahenta/<int:personal_data_id>/', views.Data_edit_form, name='edytujkontrahenta'),
    path('dodajuslugedofaktury/<int:invoice_id>/', views.Service_Invoice_form, name='dodajuslugedofaktury'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
