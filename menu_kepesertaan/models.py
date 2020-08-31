from django.db import models
from django.core.validators import validate_email, ValidationError
from winback.models import LokasiPekerjaan
from akun.models import Profil

# Create your models here.


# class Kabupaten_Kota(models.Model):
#     kode = models.CharField(max_length=3)
#     nama = models.CharField(max_length=30)

#     def __str__(self):
#         return self.nama


class Daftar_Perusahaan(models.Model):
    npp = models.CharField(max_length=8, verbose_name="NPP", null=True, blank=True)
    div = models.CharField(max_length=3, default='000', verbose_name="DIV", null=True, blank=True)
    nama = models.CharField(
        max_length=200, verbose_name="Nama Pemeberi Kerja/Badan Usaha", null=True, blank=True)
    blth_keps = models.DateField(verbose_name="BLTH Keps", null=True, blank=True)
    # blth_keps = models.CharField()
    total_upah = models.DecimalField(
        max_digits=13, decimal_places=2, verbose_name="Total Upah", null=True, blank=True)
    iuran_terakhir_blth = models.DateField(verbose_name="Iuran Terakhir BLTH", null=True, blank=True)
    iuran_terakhir_jlh = models.DecimalField(
        max_digits=13, decimal_places=2, verbose_name="Iuran Terakhir Jumlah", null=True, blank=True)
    alamat = models.CharField(max_length=255, verbose_name="Alamat", null=True, blank=True)
    kabupaten = models.ForeignKey(
       LokasiPekerjaan, on_delete=models.CASCADE, verbose_name="Kabupaten", null=True, blank=True)
    # kabupaten = models.CharField(max_length=50, verbose_name="Kabupaten/Kota")
    nama_pic = models.CharField(max_length=30, verbose_name="Nama PIC", null=True, blank=True)
    jabatan_pic = models.CharField(max_length=30, verbose_name="Jabatan PIC", null=True, blank=True)
    no_hp_pic = models.CharField(max_length=15, verbose_name="No HP PIC", null=True, blank=True)
    email_pic = models.EmailField(verbose_name="Email PIC", null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.npp, self.nama)
    
