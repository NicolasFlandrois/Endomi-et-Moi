# Generated by Django 3.0.7 on 2020-06-18 08:28

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painsymptom',
            name='intesity',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='painsymptom',
            name='location',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Lombaire', 'Lombaire'), ('Abdominale', 'Abdominale'), ('Intra-utérine', 'Intra-utérine'), ('Intestinale', 'Intestinale'), ('Digestive', 'Digestive'), ('Plexus', 'Plexus'), ('Aucune', 'Aucune'), ('Autres', 'Autres')], max_length=20),
        ),
    ]
