from django import forms

from .models import Aset_IT, Pemeliharaan_Umum, Pemeliharaan_Keamanaan,Pemeliharaan_Software, Pemeliharaan_Hardware, Operator


class AsetForms(forms.ModelForm):
            
    class Meta:
        model = Aset_IT
        fields = (
            'no_reg','nama_user','nama_komputer','bidang',
            'jenis_aset','merk_type','serial_num',
            'tahun_pengadaan','ip_addr','operasi_sistem',
            'lisensi_os','office','lisensi_office',
            'ocs_inventory','mac_address',
            'maintenance_done','maintenance_next'
        )

        widgets = {
            'no_reg':forms.TextInput(
                attrs={'class':'form-control col col-md-8','placeholder':'Input No Register Aset ..'}),
            'nama_user':forms.Select(
                attrs={'class':'form-control col col-md-8'}),
            'nama_komputer':forms.TextInput(
                attrs={'class':'form-control col col-md-8'}),
            'bidang':forms.Select(
                attrs={'class':'form-control col col-md-8'}),
            'jenis_aset':forms.Select(
                attrs={'class':'form-control col col-md-8'}),
            'merk_type':forms.TextInput(
                attrs={'class':'form-control col col-md-8'}),
            'serial_num':forms.TextInput(
                attrs={'class':'form-control col col-md-8','placeholder':'Input Serial Number'}),
            'tahun_pengadaan':forms.DateInput(
                attrs={'class':'form-control col col-md-8', 'type':'date'},format="DD-MM-YYYY"),
            'ip_addr':forms.TextInput(
                attrs={'class':'form-control col col-md-8'}),
            'operasi_sistem':forms.Select(
                attrs={'class':'form-control col col-md-8'}),
            'lisensi_os':forms.TextInput(
                attrs={'class':'form-control col col-md-8','placeholder':'Input Lisensi OS..'}),
            'office':forms.Select(
                attrs={'class':'form-control col col-md-8'}),
            'lisensi_office':forms.TextInput(
                attrs={'class':'form-control col col-md-8','placeholder':'Input Lisensi Office..'}),
            'ocs_inventory':forms.CheckboxInput(attrs={
                'class':'form-control'
            }),
            'mac_address':forms.TextInput(
                attrs={'class':'form-control col col-md-8', 'placeholder':'Input MAC ADDRESS'}),
            
                        
            'maintenance_done':forms.DateInput(
                attrs={'class':'form-control col col-md-8','type':'date'},format="DD-MM-YYYY"),
            'maintenance_next':forms.DateInput(
                attrs={'class':'form-control col col-md-8','type':'date'},format="DD-MM-YYYY")
        }

class UmumForm(forms.ModelForm):
    class Meta:
        model = Pemeliharaan_Umum
        fields = [
            'rescue_disc','update_windows',
            'clear_browser_cache','cek_ruangan_hdd',
            'cek_konfigurasi_startup','kosongkan_recycle_bin'
        ]

        widgets = {
            'rescue_disc':forms.CheckboxInput(
                attrs={'class':'form-control'}),
            'update_windows':forms.CheckboxInput(
                attrs={'class':'form-control'}),
            'clear_browser_cache':forms.CheckboxInput(
                attrs={'class':'form-control'}),
            'cek_ruangan_hdd':forms.CheckboxInput(
                attrs={'class':'form-control'}),
            'cek_konfigurasi_startup':forms.CheckboxInput(
                attrs={'class':'form-control'}),
            'kosongkan_recycle_bin':forms.CheckboxInput(
                attrs={'class':'form-control'}),                
        }

class KeamananForm(forms.ModelForm):
    class Meta:
        model = Pemeliharaan_Keamanaan
        fields = [
            'update_antivirus','full_scanning'
        ]

        widgets = {
            'update_antivirus':forms.CheckboxInput(
                attrs={'class':'form-control'}),
            'full_scanning':forms.CheckboxInput(
                attrs={'class':'form-control'}),
        }

class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Pemeliharaan_Software
        fields = [
            'disk_cleanup','disk_defragment',
            'uninstall_app_tdk_perlu','restart_pc'
        ]

        widgets = {
            'disk_cleanup':forms.CheckboxInput(
                attrs={'class':'form-control'}),
            'disk_defragment':forms.CheckboxInput(
                attrs={'class':'form-control'}),
            'uninstall_app_tdk_perlu':forms.CheckboxInput(
                attrs={'class':'form-control'}),
            'restart_pc':forms.CheckboxInput(
                attrs={'class':'form-control'}),
        }

class HardwareForm(forms.ModelForm):
    class Meta:
        model = Pemeliharaan_Hardware
        fields = [
            'dead_pixel_monitor','keyboard_mouse',
            'cacat_casing','fungsi_cooler_fan',
            'pembersihan_casing','cleaning_keyboard_mouse',
            'cleaning_cooler_fan','merapikan_kabel'
        ]

        widgets = {
            'dead_pixel_monitor':forms.CheckboxInput(
                attrs={'class':'form-control'}),
            'keyboard_mouse':forms.CheckboxInput(
                attrs={'class':'form-control'}),
            'cacat_casing':forms.CheckboxInput(
                attrs={'class':'form-control'}),
            'fungsi_cooler_fan':forms.CheckboxInput(
                attrs={'class':'form-control'}),
            'pembersihan_casing':forms.CheckboxInput(
                attrs={'class':'form-control'}),
            'cleaning_keyboard_mouse':forms.CheckboxInput(
                attrs={'class':'form-control'}),
            'cleaning_cooler_fan':forms.CheckboxInput(
                attrs={'class':'form-control'}),
            'merapikan_kabel':forms.CheckboxInput(
                attrs={'class':'form-control'}),
        }

class OperatorForm(forms.ModelForm):
    class Meta:
        model = Operator
        fields = [
            'nama','perusahaan'
        ]

        widgets = {
            'nama':forms.TextInput(
                attrs={'class':'form-control col col-sm-8','placeholder':'Input Nama Operator'}),
            'perusahaan':forms.TextInput(
                attrs={'class':'form-control col col-sm-8','placeholder':'Input Nama Perusahaan'}),
        }