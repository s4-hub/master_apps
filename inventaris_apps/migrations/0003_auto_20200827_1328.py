# Generated by Django 3.0.5 on 2020-08-27 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaris_apps', '0002_auto_20200827_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aset_it',
            name='mac_address',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='MAC ADDRESS'),
        ),
        migrations.AlterField(
            model_name='aset_it',
            name='ocs_inventory',
            field=models.BooleanField(choices=[('T', 'TIDAK'), ('Y', 'YA')], default=False, verbose_name='OCS INVENTORY'),
        ),
        migrations.AlterField(
            model_name='pemeliharaan_hardware',
            name='cacat_casing',
            field=models.BooleanField(blank=True, choices=[('T', 'TIDAK'), ('Y', 'YA')], default=False, null=True, verbose_name='CEK CACAT PADA CASING'),
        ),
        migrations.AlterField(
            model_name='pemeliharaan_hardware',
            name='cleaning_cooler_fan',
            field=models.BooleanField(blank=True, choices=[('T', 'TIDAK'), ('Y', 'YA')], default=False, null=True, verbose_name='PEMBERSIHAN KIPAS PENDINGIN'),
        ),
        migrations.AlterField(
            model_name='pemeliharaan_hardware',
            name='cleaning_keyboard_mouse',
            field=models.BooleanField(blank=True, choices=[('T', 'TIDAK'), ('Y', 'YA')], default=False, null=True, verbose_name='PEMBERSIHAN KEYBOARD DAN MOUSE'),
        ),
        migrations.AlterField(
            model_name='pemeliharaan_hardware',
            name='dead_pixel_monitor',
            field=models.BooleanField(blank=True, choices=[('T', 'TIDAK'), ('Y', 'YA')], default=False, null=True, verbose_name='CEK DEAD PIXEL MONITOR'),
        ),
        migrations.AlterField(
            model_name='pemeliharaan_hardware',
            name='fungsi_cooler_fan',
            field=models.BooleanField(blank=True, choices=[('T', 'TIDAK'), ('Y', 'YA')], default=False, null=True, verbose_name='CEK FUNGSI KIPAS PENDINGIN'),
        ),
        migrations.AlterField(
            model_name='pemeliharaan_hardware',
            name='keyboard_mouse',
            field=models.BooleanField(blank=True, choices=[('T', 'TIDAK'), ('Y', 'YA')], default=False, null=True, verbose_name='CEK FUNGSI KEYBOARD DAN MOUSE'),
        ),
        migrations.AlterField(
            model_name='pemeliharaan_hardware',
            name='merapikan_kabel',
            field=models.BooleanField(blank=True, choices=[('T', 'TIDAK'), ('Y', 'YA')], default=False, null=True, verbose_name='MERAPIKAN KABEL'),
        ),
        migrations.AlterField(
            model_name='pemeliharaan_hardware',
            name='pembersihan_casing',
            field=models.BooleanField(blank=True, choices=[('T', 'TIDAK'), ('Y', 'YA')], default=False, null=True, verbose_name='PEMBERSIHAN CASING'),
        ),
        migrations.AlterField(
            model_name='pemeliharaan_keamanaan',
            name='full_scanning',
            field=models.BooleanField(blank=True, choices=[('T', 'TIDAK'), ('Y', 'YA')], default=False, null=True, verbose_name='FULL SCANNING'),
        ),
        migrations.AlterField(
            model_name='pemeliharaan_keamanaan',
            name='update_antivirus',
            field=models.BooleanField(blank=True, choices=[('T', 'TIDAK'), ('Y', 'YA')], default=False, null=True, verbose_name='UPDATE ANTIVIRUS'),
        ),
        migrations.AlterField(
            model_name='pemeliharaan_software',
            name='disk_cleanup',
            field=models.BooleanField(blank=True, choices=[('T', 'TIDAK'), ('Y', 'YA')], default=False, null=True, verbose_name='DISK CLEANUP'),
        ),
        migrations.AlterField(
            model_name='pemeliharaan_software',
            name='disk_defragment',
            field=models.BooleanField(blank=True, choices=[('T', 'TIDAK'), ('Y', 'YA')], default=False, null=True, verbose_name='DISK DEFRAGMENT'),
        ),
        migrations.AlterField(
            model_name='pemeliharaan_software',
            name='restart_pc',
            field=models.BooleanField(blank=True, choices=[('T', 'TIDAK'), ('Y', 'YA')], default=False, null=True, verbose_name='RESTART PC'),
        ),
        migrations.AlterField(
            model_name='pemeliharaan_software',
            name='uinstall_app_tdk_perlu',
            field=models.BooleanField(blank=True, choices=[('T', 'TIDAK'), ('Y', 'YA')], default=False, null=True, verbose_name='UNINSTALL APLIKASI YANG TIDAK PERLU'),
        ),
        migrations.AlterField(
            model_name='pemeliharaan_umum',
            name='cek_konfigurasi_startup',
            field=models.BooleanField(blank=True, choices=[('T', 'TIDAK'), ('Y', 'YA')], default=False, null=True, verbose_name='CEK KONFIGURASI STARTUP'),
        ),
        migrations.AlterField(
            model_name='pemeliharaan_umum',
            name='cek_ruangan_hdd',
            field=models.BooleanField(blank=True, choices=[('T', 'TIDAK'), ('Y', 'YA')], default=False, null=True, verbose_name='CEK RUANG HARD DISK'),
        ),
        migrations.AlterField(
            model_name='pemeliharaan_umum',
            name='clear_browser_cache',
            field=models.BooleanField(blank=True, choices=[('T', 'TIDAK'), ('Y', 'YA')], default=False, null=True, verbose_name='CLEAR BROWSER CACHE'),
        ),
        migrations.AlterField(
            model_name='pemeliharaan_umum',
            name='kosongkan_recycle_bin',
            field=models.BooleanField(blank=True, choices=[('T', 'TIDAK'), ('Y', 'YA')], default=False, null=True, verbose_name='KOSONGKAN RECYCLE BIN'),
        ),
        migrations.AlterField(
            model_name='pemeliharaan_umum',
            name='rescue_disc',
            field=models.BooleanField(blank=True, choices=[('T', 'TIDAK'), ('Y', 'YA')], default=False, null=True, verbose_name='BUAT/UPDATE RESCUE DISC'),
        ),
        migrations.AlterField(
            model_name='pemeliharaan_umum',
            name='update_windows',
            field=models.BooleanField(blank=True, choices=[('T', 'TIDAK'), ('Y', 'YA')], default=False, null=True, verbose_name='UPDATE WINDOWS'),
        ),
    ]
