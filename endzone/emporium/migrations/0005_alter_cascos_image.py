# Generated by Django 3.2.3 on 2023-05-24 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emporium', '0004_alter_cascos_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cascos',
            name='image',
            field=models.FileField(upload_to='images_cascos/'),
        ),
    ]
