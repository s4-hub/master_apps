from django.contrib import admin

from .models import Antol
# Register your models here.


@admin.register(Antol)
class AntolAdmin(admin.ModelAdmin):
    list_display = (
        'kode', 'nik', 'kpj',
        'nama', 'no_hp', 'email',
        'shift', 'kegiatan', 'tgl_antol'
    )
