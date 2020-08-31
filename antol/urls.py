from django.urls import path

from . import views

app_name = 'antol'
urlpatterns = [
    path('', views.index, name='home'),
    path('upload/', views.csv_to_models, name='upload'),
    path('simpan/', views.simpan, name='simpan'),
    path('pesan/<int:pk>/',views.send_wa, name='pesan'),
    path('pesan/template/', views.template_pesan, name='template'),
]
