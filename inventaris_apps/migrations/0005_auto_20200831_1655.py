# Generated by Django 3.0.5 on 2020-08-31 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventaris_apps', '0004_aset_it_nama_komputer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pemeliharaan_software',
            old_name='uinstall_app_tdk_perlu',
            new_name='uninstall_app_tdk_perlu',
        ),
    ]
