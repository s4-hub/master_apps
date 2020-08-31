from django.db import models
from django.contrib.auth.models import User
# Create your models here.

PILIHAN = (
    (1,'Tersedia'),
    (2,'Kosong'),
)


class KategoriProduk(models.Model):
    nama = models.CharField(max_length=30)

    def __str__(self):
        return self.nama
    

class SatuanProduk(models.Model):
    kode = models.CharField(max_length=5)
    nama = models.CharField(max_length=30)

    def __str__(self):
        return self.kode
    

class Produk(models.Model):
    kategori = models.ForeignKey(KategoriProduk, on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)
    jumlah = models.IntegerField()
    per_unit = models.IntegerField(blank=True, null=True)
    satuan = models.ForeignKey(SatuanProduk, on_delete=models.CASCADE)
    harga = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    def status(self):
        if self.jumlah <= 0:
            status = 'Y'
        else:
            status = 'N'
        return '{}'.format(status)
    
    def total_unit(self):

        return '{}'.format(self.jumlah*self.per_unit)

    def total(self):
        
        return '{}'.format(self.jumlah*self.harga)
    
    def __str__(self):
        return '{}'.format(self.nama)
    

class Permintaan(models.Model):
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jumlah = models.IntegerField()
    # sisa = models.IntegerField(default=0)
    tgl = models.DateTimeField(auto_now_add=True)

    def sisa(self):

        self.sisa = 0

        if self.sisa:

            self.sisa = Produk.total_unit - self.jumlah
        else:
            return '{}'.format(Produk.jumlah)
    
    def HargaSisa(self):
        unit = Produk.harga/Produk.per_unit
        self.HargaSisa = self.sisa * unit
        return '{}'.format(self.HargaSisa)