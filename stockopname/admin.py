from django.contrib import admin

from .models import Permintaan, Produk, KategoriProduk, SatuanProduk

admin.site.register(Produk)
admin.site.register(Permintaan)
admin.site.register(KategoriProduk)
admin.site.register(SatuanProduk)