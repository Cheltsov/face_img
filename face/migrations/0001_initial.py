# Generated by Django 2.2.6 on 2019-10-19 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_1', models.ImageField(upload_to='files/')),
                ('img_2', models.ImageField(upload_to='files/')),
            ],
        ),
    ]
