from django.urls import path

from . import views

app_name = 'stockopname'
urlpatterns = [
    path('', views.index, name='home'),
    path('stock/input', views.inputstok, name='input'),
    path('stock/kategori', views.inputkategori, name='kategori'),
    path('stock/satuan',views.inputsatuan, name='satuan'),
    # path('upload/',views.baca_txt, name='upload'),
]
