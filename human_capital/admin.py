from django.contrib import admin

from .models import Karyawan, Karir

@admin.register(Karyawan)
class AdminKaryawan(admin.ModelAdmin):
    list_display = (
        'karyawan','nik','tgl_lhr',
        'gol_darah','alamat','status','istri',
        'tgl_lhr','anak_1','tgl_lhr_1',
        'anak_2','tgl_lhr_2'
    )

@admin.register(Karir)
class AdminKarir(admin.ModelAdmin):
    list_display = (
        'karyawan_k','status_karir','tgl_efektif',
        'job_desk','unit_kerja','masa_kerja'
    )