from django.urls import path

from . import views

app_name = 'aset'
urlpatterns = [
    path('', views.index, name='home'),
    path('tambah/', views.input_aset, name='tambah'),
    path('export_xls/',views.export_xls, name='export'),
    path('json/',views.send_json,name='json'),
    
]
