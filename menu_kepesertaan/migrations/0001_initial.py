# Generated by Django 3.0.5 on 2020-08-27 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('winback', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daftar_Perusahaan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('npp', models.CharField(blank=True, max_length=8, null=True, verbose_name='NPP')),
                ('div', models.CharField(blank=True, default='000', max_length=3, null=True, verbose_name='DIV')),
                ('nama', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nama Pemeberi Kerja/Badan Usaha')),
                ('blth_keps', models.DateField(blank=True, null=True, verbose_name='BLTH Keps')),
                ('total_upah', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, verbose_name='Total Upah')),
                ('iuran_terakhir_blth', models.DateField(blank=True, null=True, verbose_name='Iuran Terakhir BLTH')),
                ('iuran_terakhir_jlh', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, verbose_name='Iuran Terakhir Jumlah')),
                ('alamat', models.CharField(blank=True, max_length=255, null=True, verbose_name='Alamat')),
                ('nama_pic', models.CharField(blank=True, max_length=30, null=True, verbose_name='Nama PIC')),
                ('jabatan_pic', models.CharField(blank=True, max_length=30, null=True, verbose_name='Jabatan PIC')),
                ('no_hp_pic', models.CharField(blank=True, max_length=15, null=True, verbose_name='No HP PIC')),
                ('email_pic', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email PIC')),
                ('kabupaten', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='winback.LokasiPekerjaan', verbose_name='Kabupaten')),
            ],
        ),
    ]
