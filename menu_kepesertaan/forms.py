from django import forms

from .models import Daftar_Perusahaan


class PerusahaanForm(forms.ModelForm):
    class Meta:
        model = Daftar_Perusahaan
        fields = (
            'npp', 'div', 'nama',
            'blth_keps', 'total_upah', 'iuran_terakhir_blth',
            'iuran_terakhir_jlh', 'alamat', 'kabupaten',
            'nama_pic', 'jabatan_pic', 'no_hp_pic', 'email_pic'
        )

        widgets = {
            'npp': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Input NPP Perusahaan'}),
            'div': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Input DIV'}),
            'nama': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Input Nama Perusahaan ..'}),
            'blth_keps': forms.DateInput(
                attrs={'class:form-control', 'type': 'date'}, format="MM-YYYY"),
            'total_upah': forms.TextInput(
                attrs={'class': 'form-control', 'placehodler': 'Input Total Upah'}),
            'iuran_terakhir_blth': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}, format="MM-YYYY"),
            'iuran_terakhir_jlh': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Input Iuran Terakhir'})
            'alamat': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Input Alamat Perusahaan ..'}),
            'kabupaten': forms.Select(
                attrs={'class': 'form-control'}),
            'nama_pic': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Input Nama PIC ..'}),
            'jabatan_pic': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Input Jabatan PIC ..'}),
            'no_hp_pic': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Input No HP PIC'}),
            'email_pic': forms.EmailInput(
                attrs={'class': 'form-control'}),
        }
