# Generated by Django 3.0.5 on 2020-08-27 05:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('akun', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Karyawan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nik', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator('^((1[1-9])|(21)|([37][1-6])|(5[1-4])|(6[1-5])|([8-9][1-2]))[0-9]{2}[0-9]{2}(([0-6][0-9])|(7[0-1]))((0[1-9])|(1[0-2]))([0-9]{2})[0-9]{4}$', message='Format NIK harus 16 Angka')])),
                ('tgl_lhr', models.DateField()),
                ('gol_darah', models.IntegerField(choices=[(1, 'A'), (2, 'B'), (3, 'AB'), (4, 'O')])),
                ('alamat', models.TextField(max_length=300)),
                ('status', models.IntegerField(blank=True, choices=[(1, 'Menikah'), (2, 'Belum Menikah')], null=True)),
                ('istri', models.CharField(blank=True, max_length=50, null=True)),
                ('tgl_i', models.DateField(blank=True, null=True)),
                ('anak_1', models.CharField(blank=True, max_length=50, null=True)),
                ('tgl_lhr_1', models.DateField(blank=True, null=True)),
                ('anak_2', models.CharField(blank=True, max_length=50, null=True)),
                ('tgl_lhr_2', models.DateField(blank=True, null=True)),
                ('karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='username', to='akun.Profil')),
            ],
        ),
        migrations.CreateModel(
            name='Karir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_karir', models.IntegerField(choices=[(1, 'Permanent'), (2, 'Unpermanent')])),
                ('tgl_efektif', models.DateField()),
                ('job_desk', models.IntegerField(choices=[(1, ((1, 'Kabid Kepesertaan'), (2, 'Kabid Pelayanan')))])),
                ('unit_kerja', models.CharField(choices=[('A09', 'Kacab Langsa')], max_length=3)),
                ('karyawan_k', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_capital.Karyawan')),
            ],
        ),
    ]
