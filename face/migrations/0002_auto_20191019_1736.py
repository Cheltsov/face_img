# Generated by Django 2.2.6 on 2019-10-19 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='img_1',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='photo',
            name='img_2',
            field=models.ImageField(upload_to=''),
        ),
    ]