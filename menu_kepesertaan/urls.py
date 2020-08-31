from django.urls import path

from . import views

app_name = 'kepesertaan'
urlpatterns = [
    path('', views.index, name='home'),
    # path('upload/', views.upload_pdf, name='upload'),
    # path('upload/', views.csv_to_models, name='upload'),
    # path('upload/',views.baca_csv, name='upload'),
    path('upload/',views.baca_txt, name='upload'),
]
