# Generated by Django 2.2.1 on 2019-06-03 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20190603_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(default='', max_length=10240, verbose_name='详细'),
        ),
    ]