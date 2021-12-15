from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'faktury'
urlpatterns = [
    path('lista/', views.list, name='lista'),
    path('listakontrahentow/', views.traders_list, name='listakontrahentow'),
    path('listaproduktow/', views.service_list, name='listaproduktow'),
    path('dodajmiasto/', views.City_form, name='dodajmiasto'),
    path('dodajadres/', views.Address_form, name='dodajadres'),
    path('dodajdane/', views.Personal_Data_form, name='dodajdane'),
    path('dodajusluge/', views.Service_form, name='dodajusluge'),
    path('dodajfakture/', views.Invoice_form, name='dodajfakture'),
    path('dodajskan/', views.upload_with_image, name='dodajskan'),
    path('faktura/<int:invoice_id>/', views.Invoice_display, name='faktura'),
    path('usunfakture/<int:invoice_id>/', views.Invoice_delete_form, name='usunfakture'),
    path('edytujfakture/<int:invoice_id>/', views.Invoice_edit_form, name='edytujfakture'),
    path('usunprodukt/<int:service_id>/', views.Service_delete_form, name='usunprodukt'),
    path('edytujprodukt/<int:service_id>/', views.Service_edit_form, name='edytujprodukt'),
    path('usunkontahenta/<int:personal_data_id>/', views.Data_delete_form, name='usunkontahenta'),
    path('edytujkontrahenta/<int:personal_data_id>/', views.Data_edit_form, name='edytujkontrahenta'),
    path('dodajuslugedofaktury/<int:invoice_id>/', views.Service_Invoice_form, name='dodajuslugedofaktury'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

