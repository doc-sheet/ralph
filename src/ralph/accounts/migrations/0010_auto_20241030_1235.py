# Generated by Django 2.0.13 on 2024-10-30 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20240621_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ralphuser',
            name='department',
            field=models.CharField(blank=True, max_length=128, verbose_name='department'),
        ),
    ]