from django.contrib import admin


from .models import Aset_IT, bidang, jenis_aset, Sistem_Operasi, Office, Pemeliharaan_Hardware, Pemeliharaan_Keamanaan, Pemeliharaan_Software, Pemeliharaan_Umum, Operator
# Register your models here.

admin.site.register(Aset_IT)
admin.site.register(bidang)
admin.site.register(jenis_aset)
admin.site.register(Sistem_Operasi)
admin.site.register(Office)
admin.site.register(Pemeliharaan_Umum)
admin.site.register(Pemeliharaan_Keamanaan)
admin.site.register(Pemeliharaan_Software)
admin.site.register(Pemeliharaan_Hardware)
admin.site.register(Operator)