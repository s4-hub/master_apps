from django.urls import path

from human_capital.views import UserAutocomplete

from . import views

app_name = 'hcp'
urlpatterns = [
    path('',views.index,name='home'),
    path('karyawan/karir/',views.karir, name='karir'),
    path('tambah/karyawan/', views.tambah_k, name='tambah_k'),
    path('karyawan/detail/<int:pk>/', views.detail_k, name='detail_k'),
    path('karyawan/edit/<int:pk>/', views.edit_k, name='edit_k'),
    path('karyawan/hapus/<int:pk>/',views.hapus_k, name='hapus_k'),
    path('karyawan/karir/tambah/', views.tambah_karir, name='tambah_karir'),
    path('autocomplete/', UserAutocomplete.as_view(), name='profil_autocomplete'),
]
