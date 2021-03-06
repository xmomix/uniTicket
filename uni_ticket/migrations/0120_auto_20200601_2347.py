# Generated by Django 3.0.6 on 2020-06-01 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0119_auto_20200527_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(choices=[(-2, 'Molto alta'), (-1, 'Alta'), (0, 'Normale'), (1, 'Bassa'), (2, 'Molto bassa')], default=0),
        ),
        migrations.AlterField(
            model_name='ticketcategorytask',
            name='priority',
            field=models.IntegerField(choices=[(-2, 'Molto alta'), (-1, 'Alta'), (0, 'Normale'), (1, 'Bassa'), (2, 'Molto bassa')], default=0),
        ),
    ]
