from django.contrib import admin

# Register your models here.
from .models import daftar, LokasiPekerjaan, JenisPekerjaan

@admin.register(daftar)
class AdminDaftar(admin.ModelAdmin):
    list_display = [
        'nik','nama','tgl_lahir',
        'no_hp','surel','jenis_pekerjaan',
        'jenis_pekerjaan2','lokasi_pekerjaan','upah',
        'kode_paket','kode_iuran','time_stamp'
    ]

    list_filter = [
        'nama','time_stamp','nik','tgl_lahir'
    ]
@admin.register(LokasiPekerjaan)
class LokasiAdmin(admin.ModelAdmin):
    list_display = [
        'kode','nama_kota'
    ]

@admin.register(JenisPekerjaan)
class JenisAdmin(admin.ModelAdmin):
    list_display = [
        'kode','nama_pekerjaan'
    ]