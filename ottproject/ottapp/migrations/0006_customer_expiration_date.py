# Generated by Django 5.0 on 2024-01-06 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ottapp', '0005_actor_director_genre_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]