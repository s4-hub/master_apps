# Generated by Django 3.0.5 on 2020-08-28 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaris_apps', '0003_auto_20200827_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='aset_it',
            name='nama_komputer',
            field=models.CharField(default=0, max_length=30, verbose_name='NAMA KOMPUTER'),
            preserve_default=False,
        ),
    ]