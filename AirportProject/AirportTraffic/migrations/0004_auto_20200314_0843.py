# Generated by Django 3.0.4 on 2020-03-14 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AirportTraffic', '0003_auto_20200314_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='primary_key',
            field=models.IntegerField(default=0, verbose_name='primary_key'),
        ),
        migrations.AlterField(
            model_name='airport',
            name='report_period',
            field=models.CharField(max_length=100, verbose_name='report_period'),
        ),
    ]
