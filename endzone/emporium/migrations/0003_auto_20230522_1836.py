# Generated by Django 3.2.3 on 2023-05-23 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emporium', '0002_auto_20230522_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesorios',
            name='image',
            field=models.FileField(upload_to='images_accesorios/'),
        ),
        migrations.AlterField(
            model_name='cascos',
            name='image',
            field=models.FileField(upload_to='images_cascos/'),
        ),
        migrations.AlterField(
            model_name='cleats',
            name='image',
            field=models.FileField(upload_to='images_cleats/'),
        ),
    ]
