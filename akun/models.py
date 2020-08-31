from django.db import models
from django.conf import settings


class Profil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)
    npk = models.CharField(max_length=9)

    def __str__(self):
        return self.nama

   
