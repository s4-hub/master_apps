from django.urls import path

from . import views

app_name = 'winback'
urlpatterns = [
    path('input/pekerjaan/', views.InputJenis,name='input_jenis'),
    path('input/lokasi/',views.InputLokasi,name='input_lokasi'),
    path('daftar/',views.DaftarTK, name='daftar_tk'),
    path('list/pekerjaan/', views.DaftarJenis, name='list_jenis'),
    path('list/lokasi/',views.DaftarLokasi, name='list_lokasi'),
    path('upload/lokasi/', views.upload_lokasi, name='upload_lokasi'),
    path('upload/pekerjaan/', views.upload_pekerjaan, name='upload_pekerjaan'),
    path('xls/', views.export_xls,name='export_xls'),
    path('',views.ListTK,name='home'),
]
