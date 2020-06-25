from django.urls import path

from . import views

app_name = 'hcp'
urlpatterns = [
    path('',views.index,name='home'),
    path('/karir/',views.karir, name='karir'),
    path('/tambah/', views.tambah_k, name='tambah'),
]
