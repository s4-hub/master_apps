from django.db import models
from django.contrib.auth.models import User
from akun.models import Profil
from datetime import timedelta
import datetime, time

GOL_DARAH = (
    (1,'A'),
    (2,'B'),
    (3,'AB'),
    (4,'O'),
)

STATUS = (
    (1,'Menikah'),
    (2,'Belum Menikah'),
)

STATUS_KARIR = (
    (1,'Permanent'),
    (2,'Unpermanent'),
)

JOBDESK = [
    (1,(
        (1,'Kabid Kepesertaan'),
        (2,'Kabid Pelayanan'),
    )
    ),
]

class Karyawan(models.Model):
    karyawan = models.ForeignKey(Profil, on_delete=models.CASCADE)
    npk = models.CharField(max_length=9)
    nik = models.CharField(max_length=16)
    tgl_lhr = models.DateField()
    gol_darah = models.IntegerField(choices=GOL_DARAH)
    alamat = models.TextField(max_length=300)

class Keluarga(models.Model):
    k_karyawan = models.ForeignKey(Karyawan, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS)
    nama_istri = models.CharField(max_length=50, null=True, blank=True)
    tgl_lhr = models.DateField(null=True, blank=True)
    anak_1 = models.CharField(max_length=50, null=True, blank=True)
    tgl_lhr_1 = models.DateField()
    anak_2 = models.CharField(max_length=50, null=True, blank=True)
    tgl_lhr_2 = models.DateField()

class Karir(models.Model):
    karyawan_k = models.ForeignKey(Karyawan, on_delete=models.CASCADE)
    status_karir = models.IntegerField(choices=STATUS_KARIR)
    tgl_efektif = models.DateField()
    job_desk = models.IntegerField(choices=JOBDESK)
    unit_kerja = models.CharField(max_length=30)
    
    def masa_kerja(self):
        
        selisih = datetime.date.today() - self.tgl_efektif
        return '{} Tahun {} Bulan'.format(selisih.year, selisih.month)

    def status_bldp(self):
        if self.masa_kerja >= 5:
            return 'Y'
        else:
            return 'T'
    
