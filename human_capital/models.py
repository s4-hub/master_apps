from django.db import models
from django.contrib.auth.models import User
from akun.models import Profil
from django.conf import settings
from django.core.validators import RegexValidator
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

UNIT_KERJA = [
    ('A09','Kacab Langsa')
]

class Karyawan(models.Model):
    # karyawan = models.OneToOneField(settings.AUTH_USER_MODEL,
    #                             on_delete=models.CASCADE)

    karyawan = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='username')
    
    nik = models.CharField(max_length=16, validators=[RegexValidator('^((1[1-9])|(21)|([37][1-6])|(5[1-4])|(6[1-5])|([8-9][1-2]))[0-9]{2}[0-9]{2}(([0-6][0-9])|(7[0-1]))((0[1-9])|(1[0-2]))([0-9]{2})[0-9]{4}$',
        message="Format NIK harus 16 Angka")])
    tgl_lhr = models.DateField()
    gol_darah = models.IntegerField(choices=GOL_DARAH)
    alamat = models.TextField(max_length=300)
    status = models.IntegerField(choices=STATUS, blank=True, null=True)
    istri = models.CharField(max_length=50, null=True, blank=True)
    tgl_i = models.DateField(null=True, blank=True)
    anak_1 = models.CharField(max_length=50, blank=True, null=True)
    tgl_lhr_1 = models.DateField(null=True, blank=True)
    anak_2 = models.CharField(max_length=50, blank=True, null=True)
    tgl_lhr_2 = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nik
        
class Karir(models.Model):
    karyawan_k = models.ForeignKey(Karyawan, on_delete=models.CASCADE)
    status_karir = models.IntegerField(choices=STATUS_KARIR)
    tgl_efektif = models.DateField()
    job_desk = models.IntegerField(choices=JOBDESK)
    unit_kerja = models.CharField(max_length=3, choices=UNIT_KERJA)
    
    def masa_kerja(self):
        
        selisih = datetime.date.today() - self.tgl_efektif
        tahun = datetime.date.today().year
                        
        if (tahun % 4) or (tahun % 400) == 0:
            selisih_y = int(selisih.days/366)
            selisih_b = (selisih.days % 366) % 12
                        
        else:
            selisih_y = int(selisih.days/365)
            selisih_b = (selisih.days % 365) % 12
            
        return '{} Tahun {} Bulan'.format(selisih_y, (selisih_b))


    

    # def status_bldp(self):
    #     if self.masa_kerja < 1826.25:
    #         return 'T'
    #     else:
    #         return 'Y'                                                                                                                                                                                                                                                                                                                                                                  