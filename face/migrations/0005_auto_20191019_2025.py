# Generated by Django 2.2.6 on 2019-10-19 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0004_auto_20191019_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='evklid',
        ),
        migrations.AddField(
            model_name='photo',
            name='num_evd',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
