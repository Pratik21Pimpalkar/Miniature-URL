# Generated by Django 4.0.3 on 2022-04-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_longtoshort_hello'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('countryClicks', models.IntegerField(default=0)),
                ('deviceClicks', models.IntegerField(default=0)),
            ],
        ),
    ]
