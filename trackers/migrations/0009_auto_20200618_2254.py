# Generated by Django 3.0.7 on 2020-06-18 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0008_auto_20200618_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painsymptom',
            name='location',
            field=models.ForeignKey(max_length=20, null=True, on_delete=django.db.models.deletion.CASCADE, to='trackers.PainLocation'),
        ),
    ]
