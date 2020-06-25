from django.db import models

# Create your models here.


class Antol(models.Model):
    kode = models.IntegerField()
    kpj = models.CharField(max_length=11)
    nik = models.CharField(max_length=16)
    nama = models.CharField(max_length=50)
    no_hp = models.CharField(max_length=13)
    email = models.EmailField()
    shift = models.CharField(max_length=20)
    kegiatan = models.CharField(max_length=10)
    tgl_antol = models.DateField()

    def __str__(self):
        return self.nama
