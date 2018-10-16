from django import forms
from .models import Province


class ProvinceForm(forms.ModelForm):

    class Meta:
        model = Province
        fields = ('kode_provinsi', 'province_name', 'logo_provinsi',)