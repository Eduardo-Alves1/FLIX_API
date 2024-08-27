# Generated by Django 5.1 on 2024-08-27 19:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actors', '0002_alter_actor_birthday'),
        ('genres', '0002_rename_genre_genres'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('resume', models.TextField(blank=True, null=True)),
                ('actors', models.ManyToManyField(related_name='movies', to='actors.actor')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='movies', to='genres.genres')),
            ],
        ),
    ]
