# Generated by Django 3.0.7 on 2020-06-18 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0009_auto_20200618_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='painsymptom',
            name='location',
        ),
        migrations.CreateModel(
            name='PainLocList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pain_loc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackers.PainLocation')),
                ('pain_track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackers.PainSymptom')),
            ],
        ),
    ]
