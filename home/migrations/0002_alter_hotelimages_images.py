# Generated by Django 4.2.7 on 2024-01-28 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelimages',
            name='images',
            field=models.ImageField(upload_to='hotels'),
        ),
    ]
