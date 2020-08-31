from django import forms

from .models import LokasiPekerjaan, JenisPekerjaan, daftar

class LokasiForm(forms.ModelForm):
    class Meta:
        model = LokasiPekerjaan
        fields = ('__all__')

        widgets = {
            'kode':forms.TextInput(
                attrs={'class':'form-control'}),
            'nama_kota':forms.TextInput(
                attrs={'class':'form-control'}),
        }

class JenisForm(forms.ModelForm):
    class Meta:
        model = JenisPekerjaan
        fields = (
            'kode','nama_pekerjaan'
        )

        widgets = {
            'kode':forms.TextInput(
                attrs={'class':'form-control'}),
            'nama_pekerjaan':forms.TextInput(
                attrs={'class':'form-control'}),
        }

class DaftarForm(forms.ModelForm):
    class Meta:
        model = daftar
        fields = (
            'nik','nama','tgl_lahir',
            'no_hp','surel','jenis_pekerjaan',
            'jenis_pekerjaan2','lokasi_pekerjaan','upah',
            'kode_paket','kode_iuran'
        )

        widgets = {
            'nik':forms.TextInput(
                attrs={'class':'form-control', 'id':'nik'}),
            'nama':forms.TextInput(
                attrs={'class':'form-control'}),
            'tgl_lahir':forms.TextInput(
                attrs={'class':'form-control','type':'date'}),
            'no_hp':forms.TextInput(
                attrs={'class':'form-control'}),
            'surel':forms.EmailInput(
                attrs={'class':'form-control'}),
            'jenis_pekerjaan':forms.Select(
                attrs={'class':'form-control'}),
            'jenis_pekerjaan2':forms.Select(
                attrs={'class':'form-control'}),
            'lokasi_pekerjaan':forms.Select(
                attrs={'class':'form-control'}),
            'upah':forms.TextInput(
                attrs={'class':'form-control'}),
            'kode_paket':forms.Select(
                attrs={'class':'form-control'}),
            'kode_iuran':forms.Select(
                attrs={'class':'form-control'}),
        }