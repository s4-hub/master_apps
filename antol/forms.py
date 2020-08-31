from django import forms

from .models import TemplatePesan

class TemplateForm(forms.ModelForm):
    class Meta:
        model = TemplatePesan

        fields = ('nama','pesan',)

        widgets = {
            'nama':forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Nama Pesan ...'}),
            'pesan':forms.Textarea(
                attrs={'class':'form-control','name':'textarea-input',
                'id':'textarea-input','rows':'9',
                'placeholder':'Tuliskan Isi Pesan Template ...'}),
        }