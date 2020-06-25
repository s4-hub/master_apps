from django.db import models
from django.utils import timezone

# Create your models here.
KODE_PAKET = (
    ('T','JKK,JKM'),
    ('L','JKK,JKM,JHT')
)

KODE_IURAN = (
    (1,'1 BLN'),
    (3,'3 BLN'),
    (6,'6 BLN'),
    (12,'12 BLN')
)

class LokasiPekerjaan(models.Model):
    kode = models.CharField(max_length=4)
    nama_kota = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_kota

class JenisPekerjaan(models.Model):
    kode = models.CharField(max_length=4)
    nama_pekerjaan = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_pekerjaan
        

class daftar(models.Model):
    nik = models.CharField(max_length=16)
    nama = models.CharField(max_length=50)
    tgl_lahir = models.DateField(default=timezone.now)
    # tgl_lahir = models.CharField(max_length=10)
    no_hp = models.CharField(max_length=13)
    surel = models.EmailField(blank=True, null=True)
    jenis_pekerjaan =  models.ForeignKey(JenisPekerjaan, on_delete=models.CASCADE)
    jenis_pekerjaan2 = models.ForeignKey(JenisPekerjaan, on_delete=models.CASCADE, related_name='jenis2',null=True, blank=True)
    lokasi_pekerjaan = models.ForeignKey(LokasiPekerjaan, on_delete=models.CASCADE)
    upah = models.IntegerField()
    kode_paket = models.CharField(max_length=1, choices=KODE_PAKET)
    kode_iuran = models.IntegerField(choices=KODE_IURAN)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def total(self):
        if self.kode_paket == 'T':
            jkm = 6800
            jkk = self.upah * 0.01
            self.total = self.kode_iuran * (jkk+jkm)
        else:
            jkm = 6800
            jkk = self.upah * 0.01
            jht = self.upah * 0.02
            self.total = self.kode_iuran * (jkm+jkk+jht)

        return self.total

            