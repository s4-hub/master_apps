from django.db import models
from akun.models import Profil

# Create your models here.

YA_TIDAK = (
    ('T','TIDAK'),
    ('Y','YA'),
)

class Operator(models.Model):
    nama = models.CharField(max_length=50)
    perusahaan = models.CharField(max_length=200)

    def __str__(self):
        return '{} - {}'.format(self.nama, self.perusahaan)
   

class bidang(models.Model):
    nama = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nama

class jenis_aset(models.Model):
    nama = models.CharField(max_length=30)

    def __str__(self):
        return self.nama

class Sistem_Operasi(models.Model):
    nama = models.CharField(max_length=30)
        
    def __str__(self):
        return self.nama

class Office(models.Model):
    nama = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nama

class Pemeliharaan_Umum(models.Model):
    rescue_disc = models.BooleanField(default=False, null=True, blank=True, choices=YA_TIDAK, verbose_name='BUAT/UPDATE RESCUE DISC')
    update_windows = models.BooleanField(default=False, null=True, blank=True, choices=YA_TIDAK, verbose_name='UPDATE WINDOWS')
    clear_browser_cache = models.BooleanField(default=False, null=True, blank=True, choices=YA_TIDAK, verbose_name='CLEAR BROWSER CACHE')
    cek_ruangan_hdd = models.BooleanField(default=False, null=True, blank=True, choices=YA_TIDAK, verbose_name='CEK RUANG HARD DISK')
    cek_konfigurasi_startup = models.BooleanField(default=False, null=True, blank=True, choices=YA_TIDAK, verbose_name='CEK KONFIGURASI STARTUP')
    kosongkan_recycle_bin = models.BooleanField(default=False, null=True, blank=True, choices=YA_TIDAK, verbose_name='KOSONGKAN RECYCLE BIN')

class Pemeliharaan_Keamanaan(models.Model):
    update_antivirus = models.BooleanField(default=False, null=True, blank=True, choices=YA_TIDAK, verbose_name='UPDATE ANTIVIRUS')
    full_scanning = models.BooleanField(default=False, null=True, blank=True, choices=YA_TIDAK, verbose_name='FULL SCANNING')

class Pemeliharaan_Software(models.Model):
    disk_cleanup = models.BooleanField(default=False, null=True, blank=True, choices=YA_TIDAK, verbose_name='DISK CLEANUP')
    disk_defragment = models.BooleanField(default=False, null=True, blank=True, choices=YA_TIDAK, verbose_name='DISK DEFRAGMENT')
    uninstall_app_tdk_perlu = models.BooleanField(default=False, null=True, blank=True, choices=YA_TIDAK, verbose_name='UNINSTALL APLIKASI YANG TIDAK PERLU')
    restart_pc = models.BooleanField(default=False, null=True, blank=True, choices=YA_TIDAK, verbose_name='RESTART PC')

class Pemeliharaan_Hardware(models.Model):
    dead_pixel_monitor = models.BooleanField(default=False, null=True, blank=True, choices=YA_TIDAK, verbose_name='CEK DEAD PIXEL MONITOR')
    keyboard_mouse = models.BooleanField(default=False, null=True, blank=True, choices=YA_TIDAK, verbose_name='CEK FUNGSI KEYBOARD DAN MOUSE')
    cacat_casing = models.BooleanField(default=False, null=True, blank=True, choices=YA_TIDAK, verbose_name='CEK CACAT PADA CASING')
    fungsi_cooler_fan = models.BooleanField(default=False, null=True, blank=True, choices=YA_TIDAK, verbose_name='CEK FUNGSI KIPAS PENDINGIN')
    pembersihan_casing = models.BooleanField(default=False, null=True, blank=True, choices=YA_TIDAK, verbose_name='PEMBERSIHAN CASING')
    cleaning_keyboard_mouse = models.BooleanField(default=False, null=True, blank=True, choices=YA_TIDAK, verbose_name='PEMBERSIHAN KEYBOARD DAN MOUSE')
    cleaning_cooler_fan = models.BooleanField(default=False, null=True, blank=True, choices=YA_TIDAK, verbose_name='PEMBERSIHAN KIPAS PENDINGIN')
    merapikan_kabel = models.BooleanField(default=False, null=True, blank=True, choices=YA_TIDAK, verbose_name='MERAPIKAN KABEL')
    
class Aset_IT(models.Model):
    no_reg = models.CharField(max_length=16, verbose_name="NO REGISTER")
    nama_komputer = models.CharField(max_length=30, verbose_name="NAMA KOMPUTER")
    nama_user = models.ForeignKey(Profil, on_delete=models.CASCADE, verbose_name="PENGGUNA")
    bidang = models.ForeignKey(bidang,on_delete=models.CASCADE, verbose_name="BIDANG/BAGIAN")
    jenis_aset = models.ForeignKey(jenis_aset,on_delete=models.CASCADE, verbose_name="JENIS ASET")
    merk_type = models.CharField(max_length=100, verbose_name="MERK/TYPE")
    serial_num = models.CharField(max_length=50, verbose_name="SERIAL NUMBER")
    tahun_pengadaan = models.DateField(verbose_name="TAHUN PENGADAAN")
    ip_addr = models.GenericIPAddressField(max_length=15, verbose_name="IP ADDRESS")
    operasi_sistem = models.ForeignKey(Sistem_Operasi, on_delete=models.CASCADE, verbose_name="SISTEM OPERASI")
    lisensi_os = models.CharField(max_length=70, verbose_name="LISENSI OS")
    office = models.ForeignKey(Office,on_delete=models.CASCADE, verbose_name="OFFICE")
    lisensi_office = models.CharField(max_length=64, verbose_name="LISENSI OFFICE")
    ocs_inventory = models.BooleanField(default=False, choices=YA_TIDAK, verbose_name="OCS INVENTORY")
    mac_address = models.CharField(null=True, blank=True, max_length=17, verbose_name='MAC ADDRESS')
    pemeliharaan_umum = models.ForeignKey(Pemeliharaan_Umum, on_delete=models.CASCADE)
    pemeliharaan_keamanan = models.ForeignKey(Pemeliharaan_Keamanaan, on_delete=models.CASCADE)
    pemeliharaan_software = models.ForeignKey(Pemeliharaan_Software, on_delete=models.CASCADE)
    pemeliharaan_hardware = models.ForeignKey(Pemeliharaan_Hardware, on_delete=models.CASCADE)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    maintenance_done = models.DateField(null=True, blank=True, verbose_name="MAINTENANCE I")
    maintenance_next = models.DateField(null=True, blank=True, verbose_name="MAINTENANCE II")
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.no_reg, self.merk_type)

    
             