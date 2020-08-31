from django import forms


from .models import Produk, KategoriProduk, SatuanProduk

class InputProduk(forms.ModelForm):
    class Meta:
        model = Produk
        fields = (
            'kategori','nama','jumlah',
            'per_unit','satuan','harga'
        )

        widgets = {
            'kategori':forms.Select(
                attrs={'class':'form-control'}),
            'nama':forms.TextInput(
                attrs={'class':'form-control','placeholder':'Input Nama Produk...'}),
            'jumlah':forms.TextInput(
                attrs={'class':'form-control','placeholder':'Input Jumlah Produk...'}),
            'satuan':forms.Select(
                attrs={'class':'form-control'}),
            'harga':forms.TextInput(
                attrs={'class':'form-control'}),
        }

class KategoriProdukForm(forms.ModelForm):
    class Meta:
        model = KategoriProduk
        fields = (
            '__all__'
        )

        widgets = {
            'nama':forms.TextInput(
                attrs={'class':'form-control input-sm','placeholder':'Input Kategori Produk...'})
        }

class SatuanProdukForm(forms.ModelForm):
    class Meta:
        model = SatuanProduk
        fields = (
            '__all__'
        )

        widgets = {
            'kode':forms.TextInput(
                attrs={'class':'form-control input-sm', 'placeholder':'Input Kode...'}
            ),
            'nama':forms.TextInput(
                attrs={'class':'form-control input-sm','placeholder':'Input Nama Satuan...'}
            ),
        }