from django import forms

from .models import Karyawan, Keluarga, Karir

class KaryawanForm(forms.ModelForm):
    class Meta:
        model = Karyawan
        fields = ('__all__')

class KeluargaForm(forms.ModelForm):
    class Meta:
        model = Keluarga
        fields = ('__all__')

class KarirForm(forms.ModelForm):
    class Meta:
        model = Karir
        fields = ('__all__')
        