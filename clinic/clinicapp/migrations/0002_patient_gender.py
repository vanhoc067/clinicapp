# Generated by Django 4.0.4 on 2022-04-22 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=50),
        ),
    ]
