# Generated by Django 5.1.1 on 2024-09-11 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_remove_movie_imdb_id_remove_movie_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='custom_description',
            field=models.TextField(blank=True),
        ),
    ]