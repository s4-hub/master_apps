from django import forms
from dal import autocomplete

from .models import Karyawan, Karir

class KaryawanForm(forms.ModelForm):
    class Meta:
        model = Karyawan
        fields = (
            'karyawan','nik','tgl_lhr',
            'gol_darah','alamat','status','istri',
            'tgl_i','anak_1','tgl_lhr_1',
            'anak_2','tgl_lhr_2'
        )

        widgets = {
            'karyawan': autocomplete.ModelSelect2(
                url='hcp:profil_autocomplete'),
            
            # 'karyawan':forms.TextInput(
            #     attrs={'class':'form-control',
            #         'id':'tags', 'name':'karyawan'}),
            'nik':forms.TextInput(
                attrs={'class':'form-control',
                    'name':'nik'}),
            'tgl_lhr':forms.TextInput(
                attrs={'class':'form-control',
                    'type':'date','name':'tgl'}),
            'gol_darah':forms.Select(
                attrs={'class':'form-control',
                    'name':'gol'}),
            'alamat':forms.TextInput(
                attrs={'class':'form-control',
                    'placeholder':'Input Alamat', 'name':'alamat'}),
            'status':forms.Select(
                attrs={'class':'form-control'}),
            'nama_istri':forms.TextInput(
                attrs={'class':'form-control',
                    'placeholder':'Input Nama Istri'}),
            'tgl_i':forms.TextInput(
                attrs={'class':'form-control',
                    'id':'buttons-exmaple','type':'date'}),
            'anak_1':forms.TextInput(
                attrs={'class':'form-control',
                    'placeholder':'Input Nama Anak Pertama'}),
            'tgl_lhr_1':forms.DateInput(
                attrs={'class':'form-control','type':'date'}),
            'anak_2':forms.TextInput(
                attrs={'class':'form-control',
                    'placeholder':'Input Nama Anak Kedua'}),
            'tgl_lhr_2':forms.DateInput(
                attrs={'class':'form-control','type':'date'}),
        }

class KarirForm(forms.ModelForm):
    class Meta:
        model = Karir
        fields = (
            'karyawan_k','status_karir','tgl_efektif',
            'job_desk','unit_kerja'
        )
        
        widgets = {
            # 'karyawan_k':autocomplete.ModelSelect2(
                # url='hcp:profil_autocomplete'),
            'karyawan_k':forms.Select(
                attrs={'class':'form-control', 'disabled':'disabled'}),
            'status_karir':forms.Select(
                attrs={'class':'form-control'}),
            'tgl_efektif':forms.DateInput(
                attrs={'class':'form-control', 'type':'date'}),
            'job_desk':forms.Select(
                attrs={'class':'form-control'}),
            'unit_kerja':forms.Select(
                attrs={'class':'form-control'}),
        }