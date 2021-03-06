# Generated by Django 2.1.7 on 2019-04-11 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizational_area', '0018_organizationalstructureoffice_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationalstructureoffice',
            name='slug',
            field=models.SlugField(max_length=40),
        ),
        migrations.AlterUniqueTogether(
            name='organizationalstructureoffice',
            unique_together={('name', 'organizational_structure'), ('slug', 'organizational_structure')},
        ),
    ]
